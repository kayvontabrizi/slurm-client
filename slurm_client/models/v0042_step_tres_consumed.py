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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from slurm_client.models.v0042_tres import V0042Tres
from typing import Optional, Set
from typing_extensions import Self

class V0042StepTresConsumed(BaseModel):
    """
    V0042StepTresConsumed
    """ # noqa: E501
    max: Optional[List[V0042Tres]] = None
    min: Optional[List[V0042Tres]] = None
    average: Optional[List[V0042Tres]] = None
    total: Optional[List[V0042Tres]] = None
    __properties: ClassVar[List[str]] = ["max", "min", "average", "total"]

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
        """Create an instance of V0042StepTresConsumed from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in max (list)
        _items = []
        if self.max:
            for _item_max in self.max:
                if _item_max:
                    _items.append(_item_max.to_dict())
            _dict['max'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in min (list)
        _items = []
        if self.min:
            for _item_min in self.min:
                if _item_min:
                    _items.append(_item_min.to_dict())
            _dict['min'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in average (list)
        _items = []
        if self.average:
            for _item_average in self.average:
                if _item_average:
                    _items.append(_item_average.to_dict())
            _dict['average'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in total (list)
        _items = []
        if self.total:
            for _item_total in self.total:
                if _item_total:
                    _items.append(_item_total.to_dict())
            _dict['total'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0042StepTresConsumed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "max": [V0042Tres.from_dict(_item) for _item in obj["max"]] if obj.get("max") is not None else None,
            "min": [V0042Tres.from_dict(_item) for _item in obj["min"]] if obj.get("min") is not None else None,
            "average": [V0042Tres.from_dict(_item) for _item in obj["average"]] if obj.get("average") is not None else None,
            "total": [V0042Tres.from_dict(_item) for _item in obj["total"]] if obj.get("total") is not None else None
        })
        return _obj


