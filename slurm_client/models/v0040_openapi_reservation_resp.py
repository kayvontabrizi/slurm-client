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
from slurm_client.models.v0040_openapi_error import V0040OpenapiError
from slurm_client.models.v0040_openapi_meta import V0040OpenapiMeta
from slurm_client.models.v0040_openapi_warning import V0040OpenapiWarning
from slurm_client.models.v0040_reservation_info import V0040ReservationInfo
from slurm_client.models.v0040_uint64_no_val import V0040Uint64NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0040OpenapiReservationResp(BaseModel):
    """
    V0040OpenapiReservationResp
    """ # noqa: E501
    reservations: List[V0040ReservationInfo]
    last_update: V0040Uint64NoVal
    meta: Optional[V0040OpenapiMeta] = None
    errors: Optional[List[V0040OpenapiError]] = None
    warnings: Optional[List[V0040OpenapiWarning]] = None
    __properties: ClassVar[List[str]] = ["reservations", "last_update", "meta", "errors", "warnings"]

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
        """Create an instance of V0040OpenapiReservationResp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in reservations (list)
        _items = []
        if self.reservations:
            for _item_reservations in self.reservations:
                if _item_reservations:
                    _items.append(_item_reservations.to_dict())
            _dict['reservations'] = _items
        # override the default output from pydantic by calling `to_dict()` of last_update
        if self.last_update:
            _dict['last_update'] = self.last_update.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict['warnings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040OpenapiReservationResp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reservations": [V0040ReservationInfo.from_dict(_item) for _item in obj["reservations"]] if obj.get("reservations") is not None else None,
            "last_update": V0040Uint64NoVal.from_dict(obj["last_update"]) if obj.get("last_update") is not None else None,
            "meta": V0040OpenapiMeta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "errors": [V0040OpenapiError.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "warnings": [V0040OpenapiWarning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None
        })
        return _obj


