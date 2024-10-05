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
from openapi_client.models.v0041_update_node_msg_resume_after import V0041UpdateNodeMsgResumeAfter
from openapi_client.models.v0041_update_node_msg_weight import V0041UpdateNodeMsgWeight
from typing import Optional, Set
from typing_extensions import Self

class V0041UpdateNodeMsg(BaseModel):
    """
    V0041UpdateNodeMsg
    """ # noqa: E501
    comment: Optional[StrictStr] = Field(default=None, description="Arbitrary comment")
    cpu_bind: Optional[StrictInt] = Field(default=None, description="Default method for binding tasks to allocated CPUs")
    extra: Optional[StrictStr] = Field(default=None, description="Arbitrary string used for node filtering if extra constraints are enabled")
    features: Optional[List[StrictStr]] = Field(default=None, description="Available features")
    features_act: Optional[List[StrictStr]] = Field(default=None, description="Currently active features")
    gres: Optional[StrictStr] = Field(default=None, description="Generic resources")
    address: Optional[List[StrictStr]] = Field(default=None, description="NodeAddr, used to establish a communication path")
    hostname: Optional[List[StrictStr]] = Field(default=None, description="NodeHostname")
    name: Optional[List[StrictStr]] = Field(default=None, description="NodeName")
    state: Optional[List[StrictStr]] = Field(default=None, description="New state to assign to the node")
    reason: Optional[StrictStr] = Field(default=None, description="Reason for node being DOWN or DRAINING")
    reason_uid: Optional[StrictStr] = Field(default=None, description="User ID to associate with the reason (needed if user root is sending message)")
    resume_after: Optional[V0041UpdateNodeMsgResumeAfter] = None
    weight: Optional[V0041UpdateNodeMsgWeight] = None
    __properties: ClassVar[List[str]] = ["comment", "cpu_bind", "extra", "features", "features_act", "gres", "address", "hostname", "name", "state", "reason", "reason_uid", "resume_after", "weight"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM']):
                raise ValueError("each list item must be one of ('INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM')")
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
        """Create an instance of V0041UpdateNodeMsg from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of resume_after
        if self.resume_after:
            _dict['resume_after'] = self.resume_after.to_dict()
        # override the default output from pydantic by calling `to_dict()` of weight
        if self.weight:
            _dict['weight'] = self.weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041UpdateNodeMsg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comment": obj.get("comment"),
            "cpu_bind": obj.get("cpu_bind"),
            "extra": obj.get("extra"),
            "features": obj.get("features"),
            "features_act": obj.get("features_act"),
            "gres": obj.get("gres"),
            "address": obj.get("address"),
            "hostname": obj.get("hostname"),
            "name": obj.get("name"),
            "state": obj.get("state"),
            "reason": obj.get("reason"),
            "reason_uid": obj.get("reason_uid"),
            "resume_after": V0041UpdateNodeMsgResumeAfter.from_dict(obj["resume_after"]) if obj.get("resume_after") is not None else None,
            "weight": V0041UpdateNodeMsgWeight.from_dict(obj["weight"]) if obj.get("weight") is not None else None
        })
        return _obj


