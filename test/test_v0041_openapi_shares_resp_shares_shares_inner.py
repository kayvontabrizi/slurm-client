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

from slurm_client.models.v0041_openapi_shares_resp_shares_shares_inner import V0041OpenapiSharesRespSharesSharesInner

class TestV0041OpenapiSharesRespSharesSharesInner(unittest.TestCase):
    """V0041OpenapiSharesRespSharesSharesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSharesRespSharesSharesInner:
        """Test V0041OpenapiSharesRespSharesSharesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSharesRespSharesSharesInner`
        """
        model = V0041OpenapiSharesRespSharesSharesInner()
        if include_optional:
            return V0041OpenapiSharesRespSharesSharesInner(
                id = 56,
                cluster = '',
                name = '',
                parent = '',
                partition = '',
                shares_normalized = slurm_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_shares_normalized.v0_0_41_openapi_shares_resp_shares_shares_inner_shares_normalized(
                    set = True, 
                    infinite = True, 
                    number = 1.337, ),
                shares = slurm_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_shares.v0_0_41_openapi_shares_resp_shares_shares_inner_shares(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                tres = slurm_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres.v0_0_41_openapi_shares_resp_shares_shares_inner_tres(
                    run_seconds = [
                        slurm_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner(
                            name = '', 
                            value = slurm_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value(
                                set = True, 
                                infinite = True, 
                                number = 56, ), )
                        ], 
                    group_minutes = [
                        slurm_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner(
                            name = '', )
                        ], 
                    usage = [
                        slurm_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_usage_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_usage_inner(
                            name = '', )
                        ], ),
                effective_usage = 1.337,
                usage_normalized = slurm_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_usage_normalized.v0_0_41_openapi_shares_resp_shares_shares_inner_usage_normalized(
                    set = True, 
                    infinite = True, 
                    number = 1.337, ),
                usage = 56,
                fairshare = slurm_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_fairshare.v0_0_41_openapi_shares_resp_shares_shares_inner_fairshare(
                    factor = 1.337, 
                    level = 1.337, ),
                type = [
                    'USER'
                    ]
            )
        else:
            return V0041OpenapiSharesRespSharesSharesInner(
        )
        """

    def testV0041OpenapiSharesRespSharesSharesInner(self):
        """Test V0041OpenapiSharesRespSharesSharesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
