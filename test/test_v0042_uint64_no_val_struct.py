# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.11.0&openapi/slurmctld&openapi/slurmdbd
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from slurm_client.models.v0042_uint64_no_val_struct import V0042Uint64NoValStruct

class TestV0042Uint64NoValStruct(unittest.TestCase):
    """V0042Uint64NoValStruct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042Uint64NoValStruct:
        """Test V0042Uint64NoValStruct
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042Uint64NoValStruct`
        """
        model = V0042Uint64NoValStruct()
        if include_optional:
            return V0042Uint64NoValStruct(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0042Uint64NoValStruct(
        )
        """

    def testV0042Uint64NoValStruct(self):
        """Test V0042Uint64NoValStruct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
