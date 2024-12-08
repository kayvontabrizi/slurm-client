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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner import V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner

class TestV0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner:
        """Test V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner`
        """
        model = V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner(
                allocated = slurm_client.models.v0_0_40_accounting_allocated.v0_0_40_accounting_allocated(
                    seconds = 56, ),
                id = 56,
                start = 56,
                tres = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_tres.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_TRES(
                    type = '', 
                    name = '', 
                    id = 56, 
                    count = 56, )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner(self):
        """Test V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
