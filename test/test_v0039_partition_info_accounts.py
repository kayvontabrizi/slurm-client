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

from openapi_client.models.v0039_partition_info_accounts import V0039PartitionInfoAccounts

class TestV0039PartitionInfoAccounts(unittest.TestCase):
    """V0039PartitionInfoAccounts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039PartitionInfoAccounts:
        """Test V0039PartitionInfoAccounts
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039PartitionInfoAccounts`
        """
        model = V0039PartitionInfoAccounts()
        if include_optional:
            return V0039PartitionInfoAccounts(
                allowed = '',
                deny = ''
            )
        else:
            return V0039PartitionInfoAccounts(
        )
        """

    def testV0039PartitionInfoAccounts(self):
        """Test V0039PartitionInfoAccounts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
