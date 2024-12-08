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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_group import V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup

class TestV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup:
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup`
        """
        model = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup(
                minutes = [
                    slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                active = [
                    slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup(self):
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
