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

from slurm_client.models.v0040_user_short import V0040UserShort

class TestV0040UserShort(unittest.TestCase):
    """V0040UserShort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040UserShort:
        """Test V0040UserShort
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040UserShort`
        """
        model = V0040UserShort()
        if include_optional:
            return V0040UserShort(
                adminlevel = [
                    'Not Set'
                    ],
                defaultaccount = '',
                defaultwckey = ''
            )
        else:
            return V0040UserShort(
        )
        """

    def testV0040UserShort(self):
        """Test V0040UserShort"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()