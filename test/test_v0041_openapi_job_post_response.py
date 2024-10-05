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

from slurm_client.models.v0041_openapi_job_post_response import V0041OpenapiJobPostResponse

class TestV0041OpenapiJobPostResponse(unittest.TestCase):
    """V0041OpenapiJobPostResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobPostResponse:
        """Test V0041OpenapiJobPostResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobPostResponse`
        """
        model = V0041OpenapiJobPostResponse()
        if include_optional:
            return V0041OpenapiJobPostResponse(
                results = [
                    slurm_client.models.v0_0_41_openapi_job_post_response_results_inner.v0_0_41_openapi_job_post_response_results_inner(
                        job_id = 56, 
                        step_id = '', 
                        error = '', 
                        error_code = 56, 
                        why = '', )
                    ],
                job_id = '',
                step_id = '',
                job_submit_user_msg = '',
                meta = slurm_client.models.v0_0_41_openapi_shares_resp_meta.v0_0_41_openapi_shares_resp_meta(
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
                    slurm_client.models.v0_0_41_openapi_shares_resp_errors_inner.v0_0_41_openapi_shares_resp_errors_inner(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    slurm_client.models.v0_0_41_openapi_shares_resp_warnings_inner.v0_0_41_openapi_shares_resp_warnings_inner(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0041OpenapiJobPostResponse(
        )
        """

    def testV0041OpenapiJobPostResponse(self):
        """Test V0041OpenapiJobPostResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
