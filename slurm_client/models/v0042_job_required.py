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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from slurm_client.models.v0042_uint64_no_val_struct import V0042Uint64NoValStruct
from typing import Optional, Set
from typing_extensions import Self

class V0042JobRequired(BaseModel):
    """
    V0042JobRequired
    """ # noqa: E501
    cpus: Optional[StrictInt] = Field(default=None, description="Minimum number of CPUs required", alias="CPUs")
    memory_per_cpu: Optional[V0042Uint64NoValStruct] = None
    memory_per_node: Optional[V0042Uint64NoValStruct] = None
    __properties: ClassVar[List[str]] = ["CPUs", "memory_per_cpu", "memory_per_node"]

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
        """Create an instance of V0042JobRequired from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of memory_per_cpu
        if self.memory_per_cpu:
            _dict['memory_per_cpu'] = self.memory_per_cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memory_per_node
        if self.memory_per_node:
            _dict['memory_per_node'] = self.memory_per_node.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0042JobRequired from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CPUs": obj.get("CPUs"),
            "memory_per_cpu": V0042Uint64NoValStruct.from_dict(obj["memory_per_cpu"]) if obj.get("memory_per_cpu") is not None else None,
            "memory_per_node": V0042Uint64NoValStruct.from_dict(obj["memory_per_node"]) if obj.get("memory_per_node") is not None else None
        })
        return _obj


