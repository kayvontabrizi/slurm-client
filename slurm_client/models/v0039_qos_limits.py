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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from slurm_client.models.v0039_qos_limits_max import V0039QosLimitsMax
from slurm_client.models.v0039_qos_limits_min import V0039QosLimitsMin
from slurm_client.models.v0039_uint32_no_val import V0039Uint32NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0039QosLimits(BaseModel):
    """
    V0039QosLimits
    """ # noqa: E501
    grace_time: Optional[V0039Uint32NoVal] = None
    max: Optional[V0039QosLimitsMax] = None
    factor: Optional[Union[StrictFloat, StrictInt]] = None
    min: Optional[V0039QosLimitsMin] = None
    __properties: ClassVar[List[str]] = ["grace_time", "max", "factor", "min"]

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
        """Create an instance of V0039QosLimits from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of grace_time
        if self.grace_time:
            _dict['grace_time'] = self.grace_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max
        if self.max:
            _dict['max'] = self.max.to_dict()
        # override the default output from pydantic by calling `to_dict()` of min
        if self.min:
            _dict['min'] = self.min.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0039QosLimits from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "grace_time": V0039Uint32NoVal.from_dict(obj["grace_time"]) if obj.get("grace_time") is not None else None,
            "max": V0039QosLimitsMax.from_dict(obj["max"]) if obj.get("max") is not None else None,
            "factor": obj.get("factor"),
            "min": V0039QosLimitsMin.from_dict(obj["min"]) if obj.get("min") is not None else None
        })
        return _obj

