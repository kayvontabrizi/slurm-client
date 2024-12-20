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

from slurm_client.models.v0042_account import V0042Account

class TestV0042Account(unittest.TestCase):
    """V0042Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042Account:
        """Test V0042Account
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042Account`
        """
        model = V0042Account()
        if include_optional:
            return V0042Account(
                associations = [
                    slurm_client.models.v0/0/42_assoc_short.v0.0.42_assoc_short(
                        account = '', 
                        cluster = '', 
                        partition = '', 
                        user = '', 
                        id = 56, )
                    ],
                coordinators = [
                    slurm_client.models.v0/0/42_coord.v0.0.42_coord(
                        name = '', 
                        direct = True, )
                    ],
                description = '',
                name = '',
                organization = '',
                flags = [
                    'DELETED'
                    ]
            )
        else:
            return V0042Account(
                description = '',
                name = '',
                organization = '',
        )
        """

    def testV0042Account(self):
        """Test V0042Account"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
