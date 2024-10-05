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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.v0040_shares_float128_tres import V0040SharesFloat128Tres
from openapi_client.models.v0040_shares_uint64_tres import V0040SharesUint64Tres
from typing import Optional, Set
from typing_extensions import Self

class V0040AssocSharesObjWrapTres(BaseModel):
    """
    V0040AssocSharesObjWrapTres
    """ # noqa: E501
    run_seconds: Optional[List[V0040SharesUint64Tres]] = None
    group_minutes: Optional[List[V0040SharesUint64Tres]] = None
    usage: Optional[List[V0040SharesFloat128Tres]] = None
    __properties: ClassVar[List[str]] = ["run_seconds", "group_minutes", "usage"]

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
        """Create an instance of V0040AssocSharesObjWrapTres from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in run_seconds (list)
        _items = []
        if self.run_seconds:
            for _item_run_seconds in self.run_seconds:
                if _item_run_seconds:
                    _items.append(_item_run_seconds.to_dict())
            _dict['run_seconds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in group_minutes (list)
        _items = []
        if self.group_minutes:
            for _item_group_minutes in self.group_minutes:
                if _item_group_minutes:
                    _items.append(_item_group_minutes.to_dict())
            _dict['group_minutes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in usage (list)
        _items = []
        if self.usage:
            for _item_usage in self.usage:
                if _item_usage:
                    _items.append(_item_usage.to_dict())
            _dict['usage'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040AssocSharesObjWrapTres from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "run_seconds": [V0040SharesUint64Tres.from_dict(_item) for _item in obj["run_seconds"]] if obj.get("run_seconds") is not None else None,
            "group_minutes": [V0040SharesUint64Tres.from_dict(_item) for _item in obj["group_minutes"]] if obj.get("group_minutes") is not None else None,
            "usage": [V0040SharesFloat128Tres.from_dict(_item) for _item in obj["usage"]] if obj.get("usage") is not None else None
        })
        return _obj


