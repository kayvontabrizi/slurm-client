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

from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_fairshare import V0041OpenapiSharesRespSharesSharesInnerFairshare

class TestV0041OpenapiSharesRespSharesSharesInnerFairshare(unittest.TestCase):
    """V0041OpenapiSharesRespSharesSharesInnerFairshare unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSharesRespSharesSharesInnerFairshare:
        """Test V0041OpenapiSharesRespSharesSharesInnerFairshare
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSharesRespSharesSharesInnerFairshare`
        """
        model = V0041OpenapiSharesRespSharesSharesInnerFairshare()
        if include_optional:
            return V0041OpenapiSharesRespSharesSharesInnerFairshare(
                factor = 1.337,
                level = 1.337
            )
        else:
            return V0041OpenapiSharesRespSharesSharesInnerFairshare(
        )
        """

    def testV0041OpenapiSharesRespSharesSharesInnerFairshare(self):
        """Test V0041OpenapiSharesRespSharesSharesInnerFairshare"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()