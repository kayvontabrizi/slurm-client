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

from slurm_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy_consumed import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed

class TestV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed(
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergyConsumed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()