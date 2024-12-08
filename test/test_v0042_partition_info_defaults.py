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

from slurm_client.models.v0042_partition_info_defaults import V0042PartitionInfoDefaults

class TestV0042PartitionInfoDefaults(unittest.TestCase):
    """V0042PartitionInfoDefaults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042PartitionInfoDefaults:
        """Test V0042PartitionInfoDefaults
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042PartitionInfoDefaults`
        """
        model = V0042PartitionInfoDefaults()
        if include_optional:
            return V0042PartitionInfoDefaults(
                memory_per_cpu = 56,
                partition_memory_per_cpu = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                partition_memory_per_node = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                time = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                job = ''
            )
        else:
            return V0042PartitionInfoDefaults(
        )
        """

    def testV0042PartitionInfoDefaults(self):
        """Test V0042PartitionInfoDefaults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
