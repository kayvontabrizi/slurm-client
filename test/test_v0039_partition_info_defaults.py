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

from openapi_client.models.v0039_partition_info_defaults import V0039PartitionInfoDefaults

class TestV0039PartitionInfoDefaults(unittest.TestCase):
    """V0039PartitionInfoDefaults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039PartitionInfoDefaults:
        """Test V0039PartitionInfoDefaults
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039PartitionInfoDefaults`
        """
        model = V0039PartitionInfoDefaults()
        if include_optional:
            return V0039PartitionInfoDefaults(
                memory_per_cpu = 56,
                time = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                job = ''
            )
        else:
            return V0039PartitionInfoDefaults(
        )
        """

    def testV0039PartitionInfoDefaults(self):
        """Test V0039PartitionInfoDefaults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()