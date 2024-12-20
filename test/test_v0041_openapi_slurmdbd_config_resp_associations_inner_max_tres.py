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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres import V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres

class TestV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres:
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres`
        """
        model = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres(
                total = [
                    slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                group = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_group.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_group(
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
                        ], ),
                minutes = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes(
                    total = [
                        slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], 
                    per = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes_per.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes_per(
                        job = [
                            slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], ), ),
                per = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_per.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_per(
                    job = [
                        slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], 
                    node = [
                        slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres(self):
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
