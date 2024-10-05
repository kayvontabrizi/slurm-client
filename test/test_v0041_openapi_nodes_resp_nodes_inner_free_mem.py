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

from slurm_client.models.v0041_openapi_nodes_resp_nodes_inner_free_mem import V0041OpenapiNodesRespNodesInnerFreeMem

class TestV0041OpenapiNodesRespNodesInnerFreeMem(unittest.TestCase):
    """V0041OpenapiNodesRespNodesInnerFreeMem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiNodesRespNodesInnerFreeMem:
        """Test V0041OpenapiNodesRespNodesInnerFreeMem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiNodesRespNodesInnerFreeMem`
        """
        model = V0041OpenapiNodesRespNodesInnerFreeMem()
        if include_optional:
            return V0041OpenapiNodesRespNodesInnerFreeMem(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiNodesRespNodesInnerFreeMem(
        )
        """

    def testV0041OpenapiNodesRespNodesInnerFreeMem(self):
        """Test V0041OpenapiNodesRespNodesInnerFreeMem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
