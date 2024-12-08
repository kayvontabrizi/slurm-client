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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from slurm_client.models.v0040_step_statistics_energy import V0040StepStatisticsEnergy
from slurm_client.models.v0042_step_statistics_cpu import V0042StepStatisticsCPU
from typing import Optional, Set
from typing_extensions import Self

class V0040StepStatistics(BaseModel):
    """
    V0040StepStatistics
    """ # noqa: E501
    cpu: Optional[V0042StepStatisticsCPU] = Field(default=None, alias="CPU")
    energy: Optional[V0040StepStatisticsEnergy] = None
    __properties: ClassVar[List[str]] = ["CPU", "energy"]

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
        """Create an instance of V0040StepStatistics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cpu
        if self.cpu:
            _dict['CPU'] = self.cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of energy
        if self.energy:
            _dict['energy'] = self.energy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040StepStatistics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CPU": V0042StepStatisticsCPU.from_dict(obj["CPU"]) if obj.get("CPU") is not None else None,
            "energy": V0040StepStatisticsEnergy.from_dict(obj["energy"]) if obj.get("energy") is not None else None
        })
        return _obj


