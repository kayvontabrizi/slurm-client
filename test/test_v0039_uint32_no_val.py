# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.05.3&openapi/v0.0.39&openapi/dbv0.0.39&openapi/slurmdbd&openapi/slurmctld
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from slurm_client.models.v0039_uint32_no_val import V0039Uint32NoVal

class TestV0039Uint32NoVal(unittest.TestCase):
    """V0039Uint32NoVal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039Uint32NoVal:
        """Test V0039Uint32NoVal
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039Uint32NoVal`
        """
        model = V0039Uint32NoVal()
        if include_optional:
            return V0039Uint32NoVal(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0039Uint32NoVal(
        )
        """

    def testV0039Uint32NoVal(self):
        """Test V0039Uint32NoVal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
