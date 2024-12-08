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
from slurm_client.models.v0042_assoc_max_jobs import V0042AssocMaxJobs
from slurm_client.models.v0042_assoc_max_per import V0042AssocMaxPer
from slurm_client.models.v0042_assoc_max_tres import V0042AssocMaxTres
from typing import Optional, Set
from typing_extensions import Self

class V0042AssocMax(BaseModel):
    """
    V0042AssocMax
    """ # noqa: E501
    jobs: Optional[V0042AssocMaxJobs] = None
    tres: Optional[V0042AssocMaxTres] = None
    per: Optional[V0042AssocMaxPer] = None
    __properties: ClassVar[List[str]] = ["jobs", "tres", "per"]

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
        """Create an instance of V0042AssocMax from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of jobs
        if self.jobs:
            _dict['jobs'] = self.jobs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tres
        if self.tres:
            _dict['tres'] = self.tres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of per
        if self.per:
            _dict['per'] = self.per.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0042AssocMax from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "jobs": V0042AssocMaxJobs.from_dict(obj["jobs"]) if obj.get("jobs") is not None else None,
            "tres": V0042AssocMaxTres.from_dict(obj["tres"]) if obj.get("tres") is not None else None,
            "per": V0042AssocMaxPer.from_dict(obj["per"]) if obj.get("per") is not None else None
        })
        return _obj


