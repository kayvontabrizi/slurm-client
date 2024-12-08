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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_usage_factor import V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor

class TestV0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor:
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor(
                set = True,
                infinite = True,
                number = 1.337
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()