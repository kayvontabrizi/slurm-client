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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing

class TestV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing:
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing(
                per = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per(
                    account = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_account.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_account(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    user = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_user.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_user(
                        set = True, 
                        infinite = True, 
                        number = 56, ), )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
