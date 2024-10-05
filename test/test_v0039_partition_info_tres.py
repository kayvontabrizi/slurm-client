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

from openapi_client.models.v0039_partition_info_tres import V0039PartitionInfoTres

class TestV0039PartitionInfoTres(unittest.TestCase):
    """V0039PartitionInfoTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039PartitionInfoTres:
        """Test V0039PartitionInfoTres
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039PartitionInfoTres`
        """
        model = V0039PartitionInfoTres()
        if include_optional:
            return V0039PartitionInfoTres(
                billing_weights = '',
                configured = ''
            )
        else:
            return V0039PartitionInfoTres(
        )
        """

    def testV0039PartitionInfoTres(self):
        """Test V0039PartitionInfoTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
