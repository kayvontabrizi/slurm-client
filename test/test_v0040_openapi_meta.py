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

from slurm_client.models.v0040_openapi_meta import V0040OpenapiMeta

class TestV0040OpenapiMeta(unittest.TestCase):
    """V0040OpenapiMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiMeta:
        """Test V0040OpenapiMeta
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiMeta`
        """
        model = V0040OpenapiMeta()
        if include_optional:
            return V0040OpenapiMeta(
                plugin = slurm_client.models.v0_0_41_openapi_shares_resp_meta_plugin.v0_0_41_openapi_shares_resp_meta_plugin(
                    type = '', 
                    name = '', 
                    data_parser = '', 
                    accounting_storage = '', ),
                client = slurm_client.models.v0_0_41_openapi_shares_resp_meta_client.v0_0_41_openapi_shares_resp_meta_client(
                    source = '', 
                    user = '', 
                    group = '', ),
                command = [
                    ''
                    ],
                slurm = slurm_client.models.v0_0_41_openapi_shares_resp_meta_slurm.v0_0_41_openapi_shares_resp_meta_slurm(
                    version = slurm_client.models.v0_0_41_openapi_shares_resp_meta_slurm_version.v0_0_41_openapi_shares_resp_meta_slurm_version(
                        major = '', 
                        micro = '', 
                        minor = '', ), 
                    release = '', 
                    cluster = '', )
            )
        else:
            return V0040OpenapiMeta(
        )
        """

    def testV0040OpenapiMeta(self):
        """Test V0040OpenapiMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
