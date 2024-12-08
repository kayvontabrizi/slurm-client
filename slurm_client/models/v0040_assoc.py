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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from slurm_client.models.v0040_accounting import V0040Accounting
from slurm_client.models.v0040_assoc_max import V0040AssocMax
from slurm_client.models.v0040_assoc_min import V0040AssocMin
from slurm_client.models.v0040_assoc_short import V0040AssocShort
from slurm_client.models.v0040_uint32_no_val import V0040Uint32NoVal
from slurm_client.models.v0042_assoc_default import V0042AssocDefault
from typing import Optional, Set
from typing_extensions import Self

class V0040Assoc(BaseModel):
    """
    V0040Assoc
    """ # noqa: E501
    accounting: Optional[List[V0040Accounting]] = None
    account: Optional[StrictStr] = Field(default=None, description="Account")
    cluster: Optional[StrictStr] = Field(default=None, description="Cluster name")
    comment: Optional[StrictStr] = Field(default=None, description="Arbitrary comment")
    default: Optional[V0042AssocDefault] = None
    flags: Optional[List[StrictStr]] = None
    max: Optional[V0040AssocMax] = None
    id: Optional[V0040AssocShort] = None
    is_default: Optional[StrictBool] = Field(default=None, description="Is default association for user")
    lineage: Optional[StrictStr] = Field(default=None, description="Complete path up the hierarchy to the root association")
    min: Optional[V0040AssocMin] = None
    parent_account: Optional[StrictStr] = Field(default=None, description="Name of parent account")
    partition: Optional[StrictStr] = Field(default=None, description="Partition name")
    priority: Optional[V0040Uint32NoVal] = None
    qos: Optional[List[StrictStr]] = Field(default=None, description="List of QOS names")
    shares_raw: Optional[StrictInt] = Field(default=None, description="Allocated shares used for fairshare calculation")
    user: StrictStr = Field(description="User name")
    __properties: ClassVar[List[str]] = ["accounting", "account", "cluster", "comment", "default", "flags", "max", "id", "is_default", "lineage", "min", "parent_account", "partition", "priority", "qos", "shares_raw", "user"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['DELETED']):
                raise ValueError("each list item must be one of ('DELETED')")
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
        """Create an instance of V0040Assoc from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in accounting (list)
        _items = []
        if self.accounting:
            for _item_accounting in self.accounting:
                if _item_accounting:
                    _items.append(_item_accounting.to_dict())
            _dict['accounting'] = _items
        # override the default output from pydantic by calling `to_dict()` of default
        if self.default:
            _dict['default'] = self.default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max
        if self.max:
            _dict['max'] = self.max.to_dict()
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of min
        if self.min:
            _dict['min'] = self.min.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040Assoc from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accounting": [V0040Accounting.from_dict(_item) for _item in obj["accounting"]] if obj.get("accounting") is not None else None,
            "account": obj.get("account"),
            "cluster": obj.get("cluster"),
            "comment": obj.get("comment"),
            "default": V0042AssocDefault.from_dict(obj["default"]) if obj.get("default") is not None else None,
            "flags": obj.get("flags"),
            "max": V0040AssocMax.from_dict(obj["max"]) if obj.get("max") is not None else None,
            "id": V0040AssocShort.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "is_default": obj.get("is_default"),
            "lineage": obj.get("lineage"),
            "min": V0040AssocMin.from_dict(obj["min"]) if obj.get("min") is not None else None,
            "parent_account": obj.get("parent_account"),
            "partition": obj.get("partition"),
            "priority": V0040Uint32NoVal.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "qos": obj.get("qos"),
            "shares_raw": obj.get("shares_raw"),
            "user": obj.get("user")
        })
        return _obj


