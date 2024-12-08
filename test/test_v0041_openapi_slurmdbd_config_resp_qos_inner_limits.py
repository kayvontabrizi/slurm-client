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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits import V0041OpenapiSlurmdbdConfigRespQosInnerLimits

class TestV0041OpenapiSlurmdbdConfigRespQosInnerLimits(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespQosInnerLimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespQosInnerLimits:
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimits
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInnerLimits`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInnerLimits()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimits(
                grace_time = 56,
                max = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max(
                    active_jobs = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs(
                        accruing = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        count = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count(
                            set = True, 
                            infinite = True, 
                            number = 56, ), ), 
                    tres = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres(
                        total = [
                            slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                type = '', 
                                name = '', 
                                id = 56, )
                            ], 
                        minutes = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes(
                            per = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per(
                                qos = [
                                    slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                        type = '', 
                                        name = '', 
                                        id = 56, )
                                    ], 
                                job = [
                                    
                                    ], 
                                account = [
                                    
                                    ], 
                                user = [
                                    
                                    ], ), ), 
                        per = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_per(
                            node = [
                                
                                ], ), ), 
                    wall_clock = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock(), 
                    jobs = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs(), 
                    accruing = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing(), ),
                factor = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor(
                    set = True, 
                    infinite = True, 
                    number = 1.337, ),
                min = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min(
                    priority_threshold = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_priority_threshold.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_priority_threshold(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    tres = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_tres.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_tres(
                        per = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_tres_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_tres_per(
                            job = [
                                slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                    type = '', 
                                    name = '', 
                                    id = 56, 
                                    count = 56, )
                                ], ), ), )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimits(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInnerLimits(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
