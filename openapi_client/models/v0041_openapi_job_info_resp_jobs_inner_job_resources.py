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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core import V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiJobInfoRespJobsInnerJobResources(BaseModel):
    """
    Resources used by the job
    """ # noqa: E501
    select_type: List[StrictStr] = Field(description="Scheduler consumable resource selection type")
    nodes: Optional[V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes] = None
    cpus: StrictInt = Field(description="Number of allocated CPUs")
    threads_per_core: V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore
    __properties: ClassVar[List[str]] = ["select_type", "nodes", "cpus", "threads_per_core"]

    @field_validator('select_type')
    def select_type_validate_enum(cls, value):
        """Validates the enum"""
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
        """Create an instance of V0041OpenapiJobInfoRespJobsInnerJobResources from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of threads_per_core
        if self.threads_per_core:
            _dict['threads_per_core'] = self.threads_per_core.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiJobInfoRespJobsInnerJobResources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "select_type": obj.get("select_type"),
            "nodes": V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes.from_dict(obj["nodes"]) if obj.get("nodes") is not None else None,
            "cpus": obj.get("cpus"),
            "threads_per_core": V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore.from_dict(obj["threads_per_core"]) if obj.get("threads_per_core") is not None else None
        })
        return _obj


