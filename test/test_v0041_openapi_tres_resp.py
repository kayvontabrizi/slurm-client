# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.11.0&openapi/slurmctld&openapi/slurmdbd
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from slurm_client.models.v0041_openapi_tres_resp import V0041OpenapiTresResp

class TestV0041OpenapiTresResp(unittest.TestCase):
    """V0041OpenapiTresResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiTresResp:
        """Test V0041OpenapiTresResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiTresResp`
        """
        model = V0041OpenapiTresResp()
        if include_optional:
            return V0041OpenapiTresResp(
                tres = [
                    slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                meta = slurm_client.models.v0_0_41_openapi_shares_resp_meta.v0_0_41_openapi_shares_resp_meta(
                    plugin = slurm_client.models.v0_0_42_openapi_meta_plugin.v0_0_42_openapi_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = slurm_client.models.v0_0_42_openapi_meta_client.v0_0_42_openapi_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = slurm_client.models.v0_0_42_openapi_meta_slurm.v0_0_42_openapi_meta_slurm(
                        version = slurm_client.models.v0_0_42_openapi_meta_slurm_version.v0_0_42_openapi_meta_slurm_version(
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
            return V0041OpenapiTresResp(
                tres = [
                    slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
        )
        """

    def testV0041OpenapiTresResp(self):
        """Test V0041OpenapiTresResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
