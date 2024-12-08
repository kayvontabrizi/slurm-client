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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer

class TestV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer:
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer(
                account = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_account.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_account(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                user = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_user.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_user(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruingPer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()