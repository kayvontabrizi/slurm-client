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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class V0042ScheduleExitFields(BaseModel):
    """
    V0042ScheduleExitFields
    """ # noqa: E501
    end_job_queue: Optional[StrictInt] = Field(default=None, description="Reached end of queue")
    default_queue_depth: Optional[StrictInt] = Field(default=None, description="Reached number of jobs allowed to be tested")
    max_job_start: Optional[StrictInt] = Field(default=None, description="Reached number of jobs allowed to start")
    max_rpc_cnt: Optional[StrictInt] = Field(default=None, description="Reached RPC limit")
    max_sched_time: Optional[StrictInt] = Field(default=None, description="Reached maximum allowed scheduler time")
    licenses: Optional[StrictInt] = Field(default=None, description="Blocked on licenses")
    __properties: ClassVar[List[str]] = ["end_job_queue", "default_queue_depth", "max_job_start", "max_rpc_cnt", "max_sched_time", "licenses"]

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
        """Create an instance of V0042ScheduleExitFields from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0042ScheduleExitFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "end_job_queue": obj.get("end_job_queue"),
            "default_queue_depth": obj.get("default_queue_depth"),
            "max_job_start": obj.get("max_job_start"),
            "max_rpc_cnt": obj.get("max_rpc_cnt"),
            "max_sched_time": obj.get("max_sched_time"),
            "licenses": obj.get("licenses")
        })
        return _obj


