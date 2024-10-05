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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.v0039_assoc_short import V0039AssocShort
from openapi_client.models.v0039_coord import V0039Coord
from openapi_client.models.v0039_user_default import V0039UserDefault
from openapi_client.models.v0039_wckey import V0039Wckey
from typing import Optional, Set
from typing_extensions import Self

class V0039User(BaseModel):
    """
    V0039User
    """ # noqa: E501
    administrator_level: Optional[List[StrictStr]] = None
    associations: Optional[List[V0039AssocShort]] = None
    coordinators: Optional[List[V0039Coord]] = None
    default: Optional[V0039UserDefault] = None
    flags: Optional[List[StrictStr]] = None
    name: StrictStr
    old_name: Optional[StrictStr] = None
    wckeys: Optional[List[V0039Wckey]] = None
    __properties: ClassVar[List[str]] = ["administrator_level", "associations", "coordinators", "default", "flags", "name", "old_name", "wckeys"]

    @field_validator('administrator_level')
    def administrator_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Not Set', 'None', 'Operator', 'Administrator']):
                raise ValueError("each list item must be one of ('Not Set', 'None', 'Operator', 'Administrator')")
        return value

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['NONE', 'DELETED']):
                raise ValueError("each list item must be one of ('NONE', 'DELETED')")
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
        """Create an instance of V0039User from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in associations (list)
        _items = []
        if self.associations:
            for _item_associations in self.associations:
                if _item_associations:
                    _items.append(_item_associations.to_dict())
            _dict['associations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in coordinators (list)
        _items = []
        if self.coordinators:
            for _item_coordinators in self.coordinators:
                if _item_coordinators:
                    _items.append(_item_coordinators.to_dict())
            _dict['coordinators'] = _items
        # override the default output from pydantic by calling `to_dict()` of default
        if self.default:
            _dict['default'] = self.default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in wckeys (list)
        _items = []
        if self.wckeys:
            for _item_wckeys in self.wckeys:
                if _item_wckeys:
                    _items.append(_item_wckeys.to_dict())
            _dict['wckeys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0039User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "administrator_level": obj.get("administrator_level"),
            "associations": [V0039AssocShort.from_dict(_item) for _item in obj["associations"]] if obj.get("associations") is not None else None,
            "coordinators": [V0039Coord.from_dict(_item) for _item in obj["coordinators"]] if obj.get("coordinators") is not None else None,
            "default": V0039UserDefault.from_dict(obj["default"]) if obj.get("default") is not None else None,
            "flags": obj.get("flags"),
            "name": obj.get("name"),
            "old_name": obj.get("old_name"),
            "wckeys": [V0039Wckey.from_dict(_item) for _item in obj["wckeys"]] if obj.get("wckeys") is not None else None
        })
        return _obj


