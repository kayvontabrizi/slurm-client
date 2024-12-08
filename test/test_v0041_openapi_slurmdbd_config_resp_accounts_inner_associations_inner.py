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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_accounts_inner_associations_inner import V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner

class TestV0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner:
        """Test V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner`
        """
        model = V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner(
                account = '',
                cluster = '',
                partition = '',
                user = '',
                id = 56
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner(
                user = '',
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner(self):
        """Test V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()