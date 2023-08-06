"""Workers for handling task running on pods."""
from __future__ import annotations

from typing import Any, List, Optional, Sequence, cast

import sqlvalidator

from bitfount.data.datasources.base_source import BaseSource
from bitfount.data.datasources.database_source import DatabaseSource
from bitfount.data.datastructure import DataStructure
from bitfount.data.exceptions import DataStructureError
from bitfount.federated.algorithms.model_algorithms.base import (
    _BaseModelAlgorithm,
    _BaseModelAlgorithmFactory,
)
from bitfount.federated.authorisation_checkers import _AuthorisationChecker
from bitfount.federated.logging import _get_federated_logger
from bitfount.federated.monitoring.monitor import task_config_update
from bitfount.federated.pod_vitals import _PodVitals
from bitfount.federated.privacy.differential import DPPodConfig
from bitfount.federated.protocols.base import (
    BaseCompatibleAlgoFactory,
    BaseProtocolFactory,
)
from bitfount.federated.transport.message_service import _BitfountMessageType
from bitfount.federated.transport.worker_transport import _WorkerMailbox
from bitfount.federated.types import (
    SerializedAlgorithm,
    SerializedProtocol,
    _DataLessAlgorithm,
)
from bitfount.federated.utils import _PROTOCOLS
from bitfount.hub.api import BitfountHub
from bitfount.schemas.utils import bf_load
from bitfount.types import _JSONDict

logger = _get_federated_logger(__name__)


class _Worker:
    """Client worker which runs a protocol locally.

    Args:
        datasource: BaseSource object.
        mailbox: Relevant mailbox.
        bitfounthub: BitfountHub object.
        authorisation: AuthorisationChecker object.
        pod_identifier: Identifier of the pod the Worker is running in.
        serialized_protocol: SerializedProtocol dictionary that the Pod has received
            from the Modeller.
        pod_vitals: PodVitals object.
        pod_dp: DPPodConfig object.
    """

    def __init__(
        self,
        datasource: BaseSource,
        mailbox: _WorkerMailbox,
        bitfounthub: BitfountHub,
        authorisation: _AuthorisationChecker,
        pod_identifier: str,
        serialized_protocol: SerializedProtocol,
        pod_vitals: Optional[_PodVitals] = None,
        pod_dp: Optional[DPPodConfig] = None,
        **_kwargs: Any,
    ):
        self.datasource = datasource
        self.mailbox = mailbox
        self.hub = bitfounthub
        self.authorisation = authorisation
        self.pod_identifier = pod_identifier
        self.serialized_protocol = serialized_protocol
        self.pod_vitals = pod_vitals
        self._pod_dp = pod_dp

    async def run(self) -> None:
        """Calls relevant training procedure and sends back weights/results."""
        # Send task to Monitor service. This is done regardless of whether or not
        # the task is accepted. This method is being run in a task monitor context
        # manager so no need to set the task monitor prior to sending.
        task_config_update(dict(self.serialized_protocol))

        # Check authorisation with access manager
        authorisation_errors = await self.authorisation.check_authorisation()

        if authorisation_errors.messages:
            # Reject task, as there were errors
            await self.mailbox.reject_task(
                authorisation_errors.messages,
            )
            return

        # Accept task and inform modeller
        logger.info("Task accepted, informing modeller.")
        await self.mailbox.accept_task()

        # Wait for Modeller to give the green light to start the task
        await self.mailbox.get_task_start_update()

        # Update hub instance if BitfountModelReference
        algorithm = self.serialized_protocol["algorithm"]
        if not isinstance(self.serialized_protocol["algorithm"], list):
            algorithm = [cast(SerializedAlgorithm, algorithm)]

        algorithm = cast(List[SerializedAlgorithm], algorithm)
        for algo in algorithm:
            if model := algo.get("model"):
                if model["class_name"] == "BitfountModelReference":
                    logger.debug("Patching model reference hub.")
                    model["hub"] = self.hub

        # Deserialize protocol only after task has been accepted just to be safe
        protocol = cast(
            BaseProtocolFactory,
            bf_load(cast(_JSONDict, self.serialized_protocol), _PROTOCOLS),
        )

        # Load data according to model datastructure if one exists.
        # For multi-algorithm protocols, we assume that all algorithm models have the
        # same datastructure.
        datastructure: Optional[DataStructure] = None
        algorithm_ = protocol.algorithm
        if not isinstance(algorithm_, Sequence):
            algorithm_ = [algorithm_]

        algorithm_ = cast(List[BaseCompatibleAlgoFactory], algorithm_)
        for algo_ in algorithm_:
            if isinstance(algo_, _BaseModelAlgorithmFactory):
                datastructure = algo_.model.datastructure

            if not isinstance(algo_, _DataLessAlgorithm):
                # We execute the query directly on the db connection,
                # or load the data at runtime for a csv.
                # TODO: [NO_TICKET: Reason] No ticket created yet. Add the private sql query algorithm here as well. # noqa: B950
                self._load_data_for_worker(datastructure=datastructure)

        # Calling the `worker` method on the protocol also calls the `worker` method on
        # underlying objects such as the algorithm and aggregator. The algorithm
        # `worker` method will also download the model from the Hub if it is a
        # `BitfountModelReference`
        worker_protocol = protocol.worker(mailbox=self.mailbox, hub=self.hub)

        # If the algorithm is a model algorithm, then we need to pass the pod identifier
        # to the model so that it can extract the relevant information from the
        # datastructure the Modeller has sent. This must be done after the worker
        # protocol has been created, so that any model references have been converted
        # to models.
        for worker_algo in worker_protocol.algorithms:
            if isinstance(worker_algo, _BaseModelAlgorithm):
                worker_algo.model.set_pod_identifier(self.pod_identifier)

        await worker_protocol.run(
            datasource=self.datasource,
            pod_dp=self._pod_dp,
            pod_vitals=self.pod_vitals,
            pod_identifier=self.mailbox.pod_identifier,
        )
        logger.info("Task complete.")
        self.mailbox.delete_all_handlers(_BitfountMessageType.LOG_MESSAGE)

    def _load_data_for_worker(
        self,
        datastructure: Optional[DataStructure] = None,
    ) -> None:
        """Load the data for the worker."""
        sql_query: Optional[str] = None
        table: Optional[str] = None
        kwargs = {}

        if datastructure:
            if datastructure.table:
                if isinstance(datastructure.table, dict):
                    if not (table := datastructure.table.get(self.pod_identifier)):
                        raise DataStructureError(
                            f"Table definition not found for {self.pod_identifier}. "
                            f"Table definitions provided in this DataStructure: "
                            f"{str(datastructure.table)}"
                        )
                    kwargs["table_name"] = table
                elif isinstance(datastructure.table, str):
                    kwargs["table_name"] = datastructure.table
            elif datastructure.query:
                if isinstance(datastructure.query, dict):
                    if not (sql_query := datastructure.query.get(self.pod_identifier)):
                        raise DataStructureError(
                            f"Query definition not found for {self.pod_identifier}. "
                            f"Query definitions provided in this DataStructure: "
                            f"{str(datastructure.query)}"
                        )
                elif isinstance(datastructure.query, str):
                    sql_query = datastructure.query
                if sql_query and sqlvalidator.parse(sql_query).is_valid():
                    if not isinstance(self.datasource, DatabaseSource):
                        raise ValueError(
                            "Incompatible DataStructure, data source pair. "
                            "DataStructure is expecting the data source to "
                            "be a DatabaseSource."
                        )
                    kwargs["sql_query"] = sql_query
        # This call loads the data for a multi-table BaseSource as specified by the
        # Modeller/DataStructure.
        self.datasource.load_data(**kwargs)
