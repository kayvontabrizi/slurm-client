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

from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_suspend_time import V0041OpenapiJobInfoRespJobsInnerSuspendTime

class TestV0041OpenapiJobInfoRespJobsInnerSuspendTime(unittest.TestCase):
    """V0041OpenapiJobInfoRespJobsInnerSuspendTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobInfoRespJobsInnerSuspendTime:
        """Test V0041OpenapiJobInfoRespJobsInnerSuspendTime
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobInfoRespJobsInnerSuspendTime`
        """
        model = V0041OpenapiJobInfoRespJobsInnerSuspendTime()
        if include_optional:
            return V0041OpenapiJobInfoRespJobsInnerSuspendTime(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiJobInfoRespJobsInnerSuspendTime(
        )
        """

    def testV0041OpenapiJobInfoRespJobsInnerSuspendTime(self):
        """Test V0041OpenapiJobInfoRespJobsInnerSuspendTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
