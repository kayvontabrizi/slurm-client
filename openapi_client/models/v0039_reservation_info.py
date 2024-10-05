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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.v0039_reservation_core_spec import V0039ReservationCoreSpec
from openapi_client.models.v0039_reservation_info_purge_completed import V0039ReservationInfoPurgeCompleted
from openapi_client.models.v0039_uint32_no_val import V0039Uint32NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0039ReservationInfo(BaseModel):
    """
    V0039ReservationInfo
    """ # noqa: E501
    accounts: Optional[StrictStr] = None
    burst_buffer: Optional[StrictStr] = None
    core_count: Optional[StrictInt] = None
    core_specializations: Optional[List[V0039ReservationCoreSpec]] = None
    end_time: Optional[StrictInt] = None
    features: Optional[StrictStr] = None
    flags: Optional[List[StrictStr]] = None
    groups: Optional[StrictStr] = None
    licenses: Optional[StrictStr] = None
    max_start_delay: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    node_count: Optional[StrictInt] = None
    node_list: Optional[StrictStr] = None
    partition: Optional[StrictStr] = None
    purge_completed: Optional[V0039ReservationInfoPurgeCompleted] = None
    start_time: Optional[StrictInt] = None
    watts: Optional[V0039Uint32NoVal] = None
    tres: Optional[StrictStr] = None
    users: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["accounts", "burst_buffer", "core_count", "core_specializations", "end_time", "features", "flags", "groups", "licenses", "max_start_delay", "name", "node_count", "node_list", "partition", "purge_completed", "start_time", "watts", "tres", "users"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['MAINT', 'NO_MAINT', 'DAILY', 'NO_DAILY', 'WEEKLY', 'NO_WEEKLY', 'IGNORE_JOBS', 'NO_IGNORE_JOBS', 'ANY_NODES', 'STATIC', 'NO_STATIC', 'PART_NODES', 'NO_PART_NODES', 'OVERLAP', 'SPEC_NODES', 'TIME_FLOAT', 'REPLACE', 'ALL_NODES', 'PURGE_COMP', 'WEEKDAY', 'NO_WEEKDAY', 'WEEKEND', 'NO_WEEKEND', 'FLEX', 'NO_FLEX', 'DURATION_PLUS', 'DURATION_MINUS', 'NO_HOLD_JOBS_AFTER_END', 'NO_PURGE_COMP', 'MAGNETIC', 'SKIP', 'HOURLY', 'NO_HOURLY', 'REOCCURRING']):
                raise ValueError("each list item must be one of ('MAINT', 'NO_MAINT', 'DAILY', 'NO_DAILY', 'WEEKLY', 'NO_WEEKLY', 'IGNORE_JOBS', 'NO_IGNORE_JOBS', 'ANY_NODES', 'STATIC', 'NO_STATIC', 'PART_NODES', 'NO_PART_NODES', 'OVERLAP', 'SPEC_NODES', 'TIME_FLOAT', 'REPLACE', 'ALL_NODES', 'PURGE_COMP', 'WEEKDAY', 'NO_WEEKDAY', 'WEEKEND', 'NO_WEEKEND', 'FLEX', 'NO_FLEX', 'DURATION_PLUS', 'DURATION_MINUS', 'NO_HOLD_JOBS_AFTER_END', 'NO_PURGE_COMP', 'MAGNETIC', 'SKIP', 'HOURLY', 'NO_HOURLY', 'REOCCURRING')")
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
        """Create an instance of V0039ReservationInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in core_specializations (list)
        _items = []
        if self.core_specializations:
            for _item_core_specializations in self.core_specializations:
                if _item_core_specializations:
                    _items.append(_item_core_specializations.to_dict())
            _dict['core_specializations'] = _items
        # override the default output from pydantic by calling `to_dict()` of purge_completed
        if self.purge_completed:
            _dict['purge_completed'] = self.purge_completed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of watts
        if self.watts:
            _dict['watts'] = self.watts.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0039ReservationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accounts": obj.get("accounts"),
            "burst_buffer": obj.get("burst_buffer"),
            "core_count": obj.get("core_count"),
            "core_specializations": [V0039ReservationCoreSpec.from_dict(_item) for _item in obj["core_specializations"]] if obj.get("core_specializations") is not None else None,
            "end_time": obj.get("end_time"),
            "features": obj.get("features"),
            "flags": obj.get("flags"),
            "groups": obj.get("groups"),
            "licenses": obj.get("licenses"),
            "max_start_delay": obj.get("max_start_delay"),
            "name": obj.get("name"),
            "node_count": obj.get("node_count"),
            "node_list": obj.get("node_list"),
            "partition": obj.get("partition"),
            "purge_completed": V0039ReservationInfoPurgeCompleted.from_dict(obj["purge_completed"]) if obj.get("purge_completed") is not None else None,
            "start_time": obj.get("start_time"),
            "watts": V0039Uint32NoVal.from_dict(obj["watts"]) if obj.get("watts") is not None else None,
            "tres": obj.get("tres"),
            "users": obj.get("users")
        })
        return _obj


