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
from slurm_client.models.v0040_float64_no_val import V0040Float64NoVal
from slurm_client.models.v0040_qos_limits import V0040QosLimits
from slurm_client.models.v0040_qos_preempt import V0040QosPreempt
from slurm_client.models.v0040_uint32_no_val import V0040Uint32NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0040Qos(BaseModel):
    """
    V0040Qos
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Arbitrary description")
    flags: Optional[List[StrictStr]] = None
    id: Optional[StrictInt] = Field(default=None, description="Unique ID")
    limits: Optional[V0040QosLimits] = None
    name: Optional[StrictStr] = Field(default=None, description="Name")
    preempt: Optional[V0040QosPreempt] = None
    priority: Optional[V0040Uint32NoVal] = None
    usage_factor: Optional[V0040Float64NoVal] = None
    usage_threshold: Optional[V0040Float64NoVal] = None
    __properties: ClassVar[List[str]] = ["description", "flags", "id", "limits", "name", "preempt", "priority", "usage_factor", "usage_threshold"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['NOT_SET', 'ADD', 'REMOVE', 'PARTITION_MINIMUM_NODE', 'PARTITION_MAXIMUM_NODE', 'PARTITION_TIME_LIMIT', 'ENFORCE_USAGE_THRESHOLD', 'NO_RESERVE', 'REQUIRED_RESERVATION', 'DENY_LIMIT', 'OVERRIDE_PARTITION_QOS', 'NO_DECAY', 'USAGE_FACTOR_SAFE', 'RELATIVE']):
                raise ValueError("each list item must be one of ('NOT_SET', 'ADD', 'REMOVE', 'PARTITION_MINIMUM_NODE', 'PARTITION_MAXIMUM_NODE', 'PARTITION_TIME_LIMIT', 'ENFORCE_USAGE_THRESHOLD', 'NO_RESERVE', 'REQUIRED_RESERVATION', 'DENY_LIMIT', 'OVERRIDE_PARTITION_QOS', 'NO_DECAY', 'USAGE_FACTOR_SAFE', 'RELATIVE')")
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
        """Create an instance of V0040Qos from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict['limits'] = self.limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of preempt
        if self.preempt:
            _dict['preempt'] = self.preempt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of usage_factor
        if self.usage_factor:
            _dict['usage_factor'] = self.usage_factor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of usage_threshold
        if self.usage_threshold:
            _dict['usage_threshold'] = self.usage_threshold.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040Qos from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "flags": obj.get("flags"),
            "id": obj.get("id"),
            "limits": V0040QosLimits.from_dict(obj["limits"]) if obj.get("limits") is not None else None,
            "name": obj.get("name"),
            "preempt": V0040QosPreempt.from_dict(obj["preempt"]) if obj.get("preempt") is not None else None,
            "priority": V0040Uint32NoVal.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "usage_factor": V0040Float64NoVal.from_dict(obj["usage_factor"]) if obj.get("usage_factor") is not None else None,
            "usage_threshold": V0040Float64NoVal.from_dict(obj["usage_threshold"]) if obj.get("usage_threshold") is not None else None
        })
        return _obj


