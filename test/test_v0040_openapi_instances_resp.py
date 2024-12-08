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

from slurm_client.models.v0040_openapi_instances_resp import V0040OpenapiInstancesResp

class TestV0040OpenapiInstancesResp(unittest.TestCase):
    """V0040OpenapiInstancesResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiInstancesResp:
        """Test V0040OpenapiInstancesResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiInstancesResp`
        """
        model = V0040OpenapiInstancesResp()
        if include_optional:
            return V0040OpenapiInstancesResp(
                instances = [
                    slurm_client.models.v0/0/40_instance.v0.0.40_instance(
                        cluster = '', 
                        extra = '', 
                        instance_id = '', 
                        instance_type = '', 
                        node_name = '', 
                        time = slurm_client.models.v0_0_42_instance_time.v0_0_42_instance_time(
                            time_end = 56, 
                            time_start = 56, ), )
                    ],
                meta = slurm_client.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
                    plugin = slurm_client.models.v0_0_42_openapi_meta_plugin.v0_0_42_openapi_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = slurm_client.models.v0_0_42_openapi_meta_client.v0_0_42_openapi_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = slurm_client.models.v0_0_42_openapi_meta_slurm.v0_0_42_openapi_meta_slurm(
                        version = slurm_client.models.v0_0_42_openapi_meta_slurm_version.v0_0_42_openapi_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', 
                        cluster = '', ), ),
                errors = [
                    slurm_client.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    slurm_client.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0040OpenapiInstancesResp(
                instances = [
                    slurm_client.models.v0/0/40_instance.v0.0.40_instance(
                        cluster = '', 
                        extra = '', 
                        instance_id = '', 
                        instance_type = '', 
                        node_name = '', 
                        time = slurm_client.models.v0_0_42_instance_time.v0_0_42_instance_time(
                            time_end = 56, 
                            time_start = 56, ), )
                    ],
        )
        """

    def testV0040OpenapiInstancesResp(self):
        """Test V0040OpenapiInstancesResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
