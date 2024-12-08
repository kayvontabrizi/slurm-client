# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.11.0&openapi/slurmctld&openapi/slurmdbd
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from slurm_client.models.v0042_partition_info_accounts import V0042PartitionInfoAccounts
from slurm_client.models.v0042_partition_info_cpus import V0042PartitionInfoCpus
from slurm_client.models.v0042_partition_info_defaults import V0042PartitionInfoDefaults
from slurm_client.models.v0042_partition_info_groups import V0042PartitionInfoGroups
from slurm_client.models.v0042_partition_info_maximums import V0042PartitionInfoMaximums
from slurm_client.models.v0042_partition_info_minimums import V0042PartitionInfoMinimums
from slurm_client.models.v0042_partition_info_nodes import V0042PartitionInfoNodes
from slurm_client.models.v0042_partition_info_partition import V0042PartitionInfoPartition
from slurm_client.models.v0042_partition_info_priority import V0042PartitionInfoPriority
from slurm_client.models.v0042_partition_info_qos import V0042PartitionInfoQos
from slurm_client.models.v0042_partition_info_timeouts import V0042PartitionInfoTimeouts
from slurm_client.models.v0042_partition_info_tres import V0042PartitionInfoTres
from slurm_client.models.v0042_uint32_no_val_struct import V0042Uint32NoValStruct
from typing import Optional, Set
from typing_extensions import Self

class V0042PartitionInfo(BaseModel):
    """
    V0042PartitionInfo
    """ # noqa: E501
    nodes: Optional[V0042PartitionInfoNodes] = None
    accounts: Optional[V0042PartitionInfoAccounts] = None
    groups: Optional[V0042PartitionInfoGroups] = None
    qos: Optional[V0042PartitionInfoQos] = None
    alternate: Optional[StrictStr] = Field(default=None, description="Alternate")
    tres: Optional[V0042PartitionInfoTres] = None
    cluster: Optional[StrictStr] = Field(default=None, description="Cluster name")
    select_type: Optional[List[StrictStr]] = None
    cpus: Optional[V0042PartitionInfoCpus] = None
    defaults: Optional[V0042PartitionInfoDefaults] = None
    grace_time: Optional[StrictInt] = Field(default=None, description="GraceTime")
    maximums: Optional[V0042PartitionInfoMaximums] = None
    minimums: Optional[V0042PartitionInfoMinimums] = None
    name: Optional[StrictStr] = Field(default=None, description="PartitionName")
    node_sets: Optional[StrictStr] = Field(default=None, description="NodeSets")
    priority: Optional[V0042PartitionInfoPriority] = None
    timeouts: Optional[V0042PartitionInfoTimeouts] = None
    partition: Optional[V0042PartitionInfoPartition] = None
    suspend_time: Optional[V0042Uint32NoValStruct] = None
    __properties: ClassVar[List[str]] = ["nodes", "accounts", "groups", "qos", "alternate", "tres", "cluster", "select_type", "cpus", "defaults", "grace_time", "maximums", "minimums", "name", "node_sets", "priority", "timeouts", "partition", "suspend_time"]

    @field_validator('select_type')
    def select_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['CPU', 'SOCKET', 'CORE', 'BOARD', 'MEMORY', 'ONE_TASK_PER_CORE', 'PACK_NODES', 'CORE_DEFAULT_DIST_BLOCK', 'LLN', 'LINEAR']):
                raise ValueError("each list item must be one of ('CPU', 'SOCKET', 'CORE', 'BOARD', 'MEMORY', 'ONE_TASK_PER_CORE', 'PACK_NODES', 'CORE_DEFAULT_DIST_BLOCK', 'LLN', 'LINEAR')")
        return value

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
        """Create an instance of V0042PartitionInfo from a JSON string"""
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
        """Create an instance of V0042PartitionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nodes": V0042PartitionInfoNodes.from_dict(obj["nodes"]) if obj.get("nodes") is not None else None,
            "accounts": V0042PartitionInfoAccounts.from_dict(obj["accounts"]) if obj.get("accounts") is not None else None,
            "groups": V0042PartitionInfoGroups.from_dict(obj["groups"]) if obj.get("groups") is not None else None,
            "qos": V0042PartitionInfoQos.from_dict(obj["qos"]) if obj.get("qos") is not None else None,
            "alternate": obj.get("alternate"),
            "tres": V0042PartitionInfoTres.from_dict(obj["tres"]) if obj.get("tres") is not None else None,
            "cluster": obj.get("cluster"),
            "select_type": obj.get("select_type"),
            "cpus": V0042PartitionInfoCpus.from_dict(obj["cpus"]) if obj.get("cpus") is not None else None,
            "defaults": V0042PartitionInfoDefaults.from_dict(obj["defaults"]) if obj.get("defaults") is not None else None,
            "grace_time": obj.get("grace_time"),
            "maximums": V0042PartitionInfoMaximums.from_dict(obj["maximums"]) if obj.get("maximums") is not None else None,
            "minimums": V0042PartitionInfoMinimums.from_dict(obj["minimums"]) if obj.get("minimums") is not None else None,
            "name": obj.get("name"),
            "node_sets": obj.get("node_sets"),
            "priority": V0042PartitionInfoPriority.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "timeouts": V0042PartitionInfoTimeouts.from_dict(obj["timeouts"]) if obj.get("timeouts") is not None else None,
            "partition": V0042PartitionInfoPartition.from_dict(obj["partition"]) if obj.get("partition") is not None else None,
            "suspend_time": V0042Uint32NoValStruct.from_dict(obj["suspend_time"]) if obj.get("suspend_time") is not None else None
        })
        return _obj

