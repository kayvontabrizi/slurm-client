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

from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_exit_code import V0041OpenapiJobInfoRespJobsInnerExitCode

class TestV0041OpenapiJobInfoRespJobsInnerExitCode(unittest.TestCase):
    """V0041OpenapiJobInfoRespJobsInnerExitCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobInfoRespJobsInnerExitCode:
        """Test V0041OpenapiJobInfoRespJobsInnerExitCode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobInfoRespJobsInnerExitCode`
        """
        model = V0041OpenapiJobInfoRespJobsInnerExitCode()
        if include_optional:
            return V0041OpenapiJobInfoRespJobsInnerExitCode(
                status = [
                    'INVALID'
                    ],
                return_code = openapi_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_return_code.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_return_code(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                signal = openapi_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal(
                    id = openapi_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal_id.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal_id(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    name = '', )
            )
        else:
            return V0041OpenapiJobInfoRespJobsInnerExitCode(
        )
        """

    def testV0041OpenapiJobInfoRespJobsInnerExitCode(self):
        """Test V0041OpenapiJobInfoRespJobsInnerExitCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
