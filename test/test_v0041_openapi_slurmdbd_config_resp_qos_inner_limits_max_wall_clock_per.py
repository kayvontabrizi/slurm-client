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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer

class TestV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer:
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer(
                qos = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_qos.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_qos(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                job = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
