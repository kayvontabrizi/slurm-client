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

from slurm_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_end import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd

class TestV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd(
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
