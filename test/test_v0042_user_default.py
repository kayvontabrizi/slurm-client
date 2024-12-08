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

from slurm_client.models.v0042_user_default import V0042UserDefault

class TestV0042UserDefault(unittest.TestCase):
    """V0042UserDefault unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042UserDefault:
        """Test V0042UserDefault
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042UserDefault`
        """
        model = V0042UserDefault()
        if include_optional:
            return V0042UserDefault(
                account = '',
                wckey = ''
            )
        else:
            return V0042UserDefault(
        )
        """

    def testV0042UserDefault(self):
        """Test V0042UserDefault"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
