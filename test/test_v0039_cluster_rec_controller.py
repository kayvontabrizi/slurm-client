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

from slurm_client.models.v0039_cluster_rec_controller import V0039ClusterRecController

class TestV0039ClusterRecController(unittest.TestCase):
    """V0039ClusterRecController unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039ClusterRecController:
        """Test V0039ClusterRecController
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039ClusterRecController`
        """
        model = V0039ClusterRecController()
        if include_optional:
            return V0039ClusterRecController(
                host = '',
                port = 56
            )
        else:
            return V0039ClusterRecController(
        )
        """

    def testV0039ClusterRecController(self):
        """Test V0039ClusterRecController"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
