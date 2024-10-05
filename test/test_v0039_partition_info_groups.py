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

from openapi_client.models.v0039_partition_info_groups import V0039PartitionInfoGroups

class TestV0039PartitionInfoGroups(unittest.TestCase):
    """V0039PartitionInfoGroups unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039PartitionInfoGroups:
        """Test V0039PartitionInfoGroups
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039PartitionInfoGroups`
        """
        model = V0039PartitionInfoGroups()
        if include_optional:
            return V0039PartitionInfoGroups(
                allowed = ''
            )
        else:
            return V0039PartitionInfoGroups(
        )
        """

    def testV0039PartitionInfoGroups(self):
        """Test V0039PartitionInfoGroups"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()