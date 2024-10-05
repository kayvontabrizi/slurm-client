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

from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_tres import V0041OpenapiSharesRespSharesSharesInnerTres

class TestV0041OpenapiSharesRespSharesSharesInnerTres(unittest.TestCase):
    """V0041OpenapiSharesRespSharesSharesInnerTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSharesRespSharesSharesInnerTres:
        """Test V0041OpenapiSharesRespSharesSharesInnerTres
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSharesRespSharesSharesInnerTres`
        """
        model = V0041OpenapiSharesRespSharesSharesInnerTres()
        if include_optional:
            return V0041OpenapiSharesRespSharesSharesInnerTres(
                run_seconds = [
                    openapi_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner(
                        name = '', 
                        value = openapi_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value(
                            set = True, 
                            infinite = True, 
                            number = 56, ), )
                    ],
                group_minutes = [
                    openapi_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner(
                        name = '', 
                        value = openapi_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value(
                            set = True, 
                            infinite = True, 
                            number = 56, ), )
                    ],
                usage = [
                    openapi_client.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_usage_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_usage_inner(
                        name = '', 
                        value = 1.337, )
                    ]
            )
        else:
            return V0041OpenapiSharesRespSharesSharesInnerTres(
        )
        """

    def testV0041OpenapiSharesRespSharesSharesInnerTres(self):
        """Test V0041OpenapiSharesRespSharesSharesInnerTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
