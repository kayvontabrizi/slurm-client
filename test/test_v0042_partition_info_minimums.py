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

from slurm_client.models.v0042_partition_info_minimums import V0042PartitionInfoMinimums

class TestV0042PartitionInfoMinimums(unittest.TestCase):
    """V0042PartitionInfoMinimums unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042PartitionInfoMinimums:
        """Test V0042PartitionInfoMinimums
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042PartitionInfoMinimums`
        """
        model = V0042PartitionInfoMinimums()
        if include_optional:
            return V0042PartitionInfoMinimums(
                nodes = 56
            )
        else:
            return V0042PartitionInfoMinimums(
        )
        """

    def testV0042PartitionInfoMinimums(self):
        """Test V0042PartitionInfoMinimums"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
