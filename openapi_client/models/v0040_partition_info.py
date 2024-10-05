# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.05.3&openapi/v0.0.39&openapi/dbv0.0.39&openapi/slurmdbd&openapi/slurmctld
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.v0040_partition_info_defaults import V0040PartitionInfoDefaults
from openapi_client.models.v0040_partition_info_maximums import V0040PartitionInfoMaximums
from openapi_client.models.v0040_partition_info_timeouts import V0040PartitionInfoTimeouts
from openapi_client.models.v0040_uint32_no_val import V0040Uint32NoVal
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_accounts import V0041OpenapiPartitionRespPartitionsInnerAccounts
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_cpus import V0041OpenapiPartitionRespPartitionsInnerCpus
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_groups import V0041OpenapiPartitionRespPartitionsInnerGroups
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_minimums import V0041OpenapiPartitionRespPartitionsInnerMinimums
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_nodes import V0041OpenapiPartitionRespPartitionsInnerNodes
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_partition import V0041OpenapiPartitionRespPartitionsInnerPartition
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_priority import V0041OpenapiPartitionRespPartitionsInnerPriority
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_qos import V0041OpenapiPartitionRespPartitionsInnerQos
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_tres import V0041OpenapiPartitionRespPartitionsInnerTres
from typing import Optional, Set
from typing_extensions import Self

class V0040PartitionInfo(BaseModel):
    """
    V0040PartitionInfo
    """ # noqa: E501
    nodes: Optional[V0041OpenapiPartitionRespPartitionsInnerNodes] = None
    accounts: Optional[V0041OpenapiPartitionRespPartitionsInnerAccounts] = None
    groups: Optional[V0041OpenapiPartitionRespPartitionsInnerGroups] = None
    qos: Optional[V0041OpenapiPartitionRespPartitionsInnerQos] = None
    alternate: Optional[StrictStr] = Field(default=None, description="Alternate")
    tres: Optional[V0041OpenapiPartitionRespPartitionsInnerTres] = None
    cluster: Optional[StrictStr] = Field(default=None, description="Cluster name")
    cpus: Optional[V0041OpenapiPartitionRespPartitionsInnerCpus] = None
    defaults: Optional[V0040PartitionInfoDefaults] = None
    grace_time: Optional[StrictInt] = Field(default=None, description="GraceTime")
    maximums: Optional[V0040PartitionInfoMaximums] = None
    minimums: Optional[V0041OpenapiPartitionRespPartitionsInnerMinimums] = None
    name: Optional[StrictStr] = Field(default=None, description="PartitionName")
    node_sets: Optional[StrictStr] = Field(default=None, description="NodeSets")
    priority: Optional[V0041OpenapiPartitionRespPartitionsInnerPriority] = None
    timeouts: Optional[V0040PartitionInfoTimeouts] = None
    partition: Optional[V0041OpenapiPartitionRespPartitionsInnerPartition] = None
    suspend_time: Optional[V0040Uint32NoVal] = None
    __properties: ClassVar[List[str]] = ["nodes", "accounts", "groups", "qos", "alternate", "tres", "cluster", "cpus", "defaults", "grace_time", "maximums", "minimums", "name", "node_sets", "priority", "timeouts", "partition", "suspend_time"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V0040PartitionInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of nodes
        if self.nodes:
            _dict['nodes'] = self.nodes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accounts
        if self.accounts:
            _dict['accounts'] = self.accounts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of groups
        if self.groups:
            _dict['groups'] = self.groups.to_dict()
        # override the default output from pydantic by calling `to_dict()` of qos
        if self.qos:
            _dict['qos'] = self.qos.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tres
        if self.tres:
            _dict['tres'] = self.tres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpus
        if self.cpus:
            _dict['cpus'] = self.cpus.to_dict()
        # override the default output from pydantic by calling `to_dict()` of defaults
        if self.defaults:
            _dict['defaults'] = self.defaults.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maximums
        if self.maximums:
            _dict['maximums'] = self.maximums.to_dict()
        # override the default output from pydantic by calling `to_dict()` of minimums
        if self.minimums:
            _dict['minimums'] = self.minimums.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timeouts
        if self.timeouts:
            _dict['timeouts'] = self.timeouts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of partition
        if self.partition:
            _dict['partition'] = self.partition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of suspend_time
        if self.suspend_time:
            _dict['suspend_time'] = self.suspend_time.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040PartitionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nodes": V0041OpenapiPartitionRespPartitionsInnerNodes.from_dict(obj["nodes"]) if obj.get("nodes") is not None else None,
            "accounts": V0041OpenapiPartitionRespPartitionsInnerAccounts.from_dict(obj["accounts"]) if obj.get("accounts") is not None else None,
            "groups": V0041OpenapiPartitionRespPartitionsInnerGroups.from_dict(obj["groups"]) if obj.get("groups") is not None else None,
            "qos": V0041OpenapiPartitionRespPartitionsInnerQos.from_dict(obj["qos"]) if obj.get("qos") is not None else None,
            "alternate": obj.get("alternate"),
            "tres": V0041OpenapiPartitionRespPartitionsInnerTres.from_dict(obj["tres"]) if obj.get("tres") is not None else None,
            "cluster": obj.get("cluster"),
            "cpus": V0041OpenapiPartitionRespPartitionsInnerCpus.from_dict(obj["cpus"]) if obj.get("cpus") is not None else None,
            "defaults": V0040PartitionInfoDefaults.from_dict(obj["defaults"]) if obj.get("defaults") is not None else None,
            "grace_time": obj.get("grace_time"),
            "maximums": V0040PartitionInfoMaximums.from_dict(obj["maximums"]) if obj.get("maximums") is not None else None,
            "minimums": V0041OpenapiPartitionRespPartitionsInnerMinimums.from_dict(obj["minimums"]) if obj.get("minimums") is not None else None,
            "name": obj.get("name"),
            "node_sets": obj.get("node_sets"),
            "priority": V0041OpenapiPartitionRespPartitionsInnerPriority.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "timeouts": V0040PartitionInfoTimeouts.from_dict(obj["timeouts"]) if obj.get("timeouts") is not None else None,
            "partition": V0041OpenapiPartitionRespPartitionsInnerPartition.from_dict(obj["partition"]) if obj.get("partition") is not None else None,
            "suspend_time": V0040Uint32NoVal.from_dict(obj["suspend_time"]) if obj.get("suspend_time") is not None else None
        })
        return _obj


