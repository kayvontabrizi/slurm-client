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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_factor import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor

class TestV0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor:
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor(
                set = True,
                infinite = True,
                number = 1.337
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
