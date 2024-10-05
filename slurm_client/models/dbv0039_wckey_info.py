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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from slurm_client.models.dbv0039_error import Dbv0039Error
from slurm_client.models.dbv0039_meta import Dbv0039Meta
from slurm_client.models.v0039_wckey import V0039Wckey
from typing import Optional, Set
from typing_extensions import Self

class Dbv0039WckeyInfo(BaseModel):
    """
    Dbv0039WckeyInfo
    """ # noqa: E501
    meta: Optional[Dbv0039Meta] = None
    errors: Optional[List[Dbv0039Error]] = Field(default=None, description="Slurm errors")
    wckeys: Optional[List[V0039Wckey]] = None
    __properties: ClassVar[List[str]] = ["meta", "errors", "wckeys"]

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
        """Create an instance of Dbv0039WckeyInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['errors'] = _items
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
        """Create an instance of Dbv0039WckeyInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "meta": Dbv0039Meta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "errors": [Dbv0039Error.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "wckeys": [V0039Wckey.from_dict(_item) for _item in obj["wckeys"]] if obj.get("wckeys") is not None else None
        })
        return _obj

