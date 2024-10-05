# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.05.3&openapi/v0.0.39&openapi/dbv0.0.39&openapi/slurmdbd&openapi/slurmctld
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from slurm_client.models.v0041_openapi_shares_resp_meta_plugin import V0041OpenapiSharesRespMetaPlugin

class TestV0041OpenapiSharesRespMetaPlugin(unittest.TestCase):
    """V0041OpenapiSharesRespMetaPlugin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSharesRespMetaPlugin:
        """Test V0041OpenapiSharesRespMetaPlugin
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSharesRespMetaPlugin`
        """
        model = V0041OpenapiSharesRespMetaPlugin()
        if include_optional:
            return V0041OpenapiSharesRespMetaPlugin(
                type = '',
                name = '',
                data_parser = '',
                accounting_storage = ''
            )
        else:
            return V0041OpenapiSharesRespMetaPlugin(
        )
        """

    def testV0041OpenapiSharesRespMetaPlugin(self):
        """Test V0041OpenapiSharesRespMetaPlugin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
