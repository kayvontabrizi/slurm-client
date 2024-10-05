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

from slurm_client.models.v0040_openapi_job_submit_response import V0040OpenapiJobSubmitResponse

class TestV0040OpenapiJobSubmitResponse(unittest.TestCase):
    """V0040OpenapiJobSubmitResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiJobSubmitResponse:
        """Test V0040OpenapiJobSubmitResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiJobSubmitResponse`
        """
        model = V0040OpenapiJobSubmitResponse()
        if include_optional:
            return V0040OpenapiJobSubmitResponse(
                result = slurm_client.models.v0/0/40_job_submit_response_msg.v0.0.40_job_submit_response_msg(
                    job_id = 56, 
                    step_id = '', 
                    error_code = 56, 
                    error = '', 
                    job_submit_user_msg = '', ),
                job_id = 56,
                step_id = '',
                job_submit_user_msg = '',
                meta = slurm_client.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
                    plugin = slurm_client.models.v0_0_41_openapi_shares_resp_meta_plugin.v0_0_41_openapi_shares_resp_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = slurm_client.models.v0_0_41_openapi_shares_resp_meta_client.v0_0_41_openapi_shares_resp_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = slurm_client.models.v0_0_41_openapi_shares_resp_meta_slurm.v0_0_41_openapi_shares_resp_meta_slurm(
                        version = slurm_client.models.v0_0_41_openapi_shares_resp_meta_slurm_version.v0_0_41_openapi_shares_resp_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', 
                        cluster = '', ), ),
                errors = [
                    slurm_client.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    slurm_client.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0040OpenapiJobSubmitResponse(
        )
        """

    def testV0040OpenapiJobSubmitResponse(self):
        """Test V0040OpenapiJobSubmitResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
