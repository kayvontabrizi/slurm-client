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

from openapi_client.models.v0041_openapi_shares_resp_warnings_inner import V0041OpenapiSharesRespWarningsInner

class TestV0041OpenapiSharesRespWarningsInner(unittest.TestCase):
    """V0041OpenapiSharesRespWarningsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSharesRespWarningsInner:
        """Test V0041OpenapiSharesRespWarningsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSharesRespWarningsInner`
        """
        model = V0041OpenapiSharesRespWarningsInner()
        if include_optional:
            return V0041OpenapiSharesRespWarningsInner(
                description = '',
                source = ''
            )
        else:
            return V0041OpenapiSharesRespWarningsInner(
        )
        """

    def testV0041OpenapiSharesRespWarningsInner(self):
        """Test V0041OpenapiSharesRespWarningsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()