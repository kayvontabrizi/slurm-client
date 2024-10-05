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

from openapi_client.models.v0039_job_update_response import V0039JobUpdateResponse

class TestV0039JobUpdateResponse(unittest.TestCase):
    """V0039JobUpdateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039JobUpdateResponse:
        """Test V0039JobUpdateResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039JobUpdateResponse`
        """
        model = V0039JobUpdateResponse()
        if include_optional:
            return V0039JobUpdateResponse(
                meta = openapi_client.models.v0/0/39_meta.v0.0.39_meta(
                    plugin = openapi_client.models.v0_0_39_meta_plugin.v0_0_39_meta_plugin(
                        type = '', 
                        name = '', ), 
                    slurm = openapi_client.models.v0_0_39_meta_slurm.v0_0_39_meta_Slurm(
                        version = openapi_client.models.v0_0_39_meta_slurm_version.v0_0_39_meta_Slurm_version(
                            major = 56, 
                            micro = 56, 
                            minor = 56, ), 
                        release = '', ), ),
                errors = [
                    openapi_client.models.v0/0/39_error.v0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    openapi_client.models.v0/0/39_warning.v0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                results = [
                    openapi_client.models.v0_0_39_job_array_response_msg_inner.v0_0_39_job_array_response_msg_inner(
                        job_id = 56, 
                        error_code = 56, 
                        error = '', 
                        why = '', )
                    ]
            )
        else:
            return V0039JobUpdateResponse(
        )
        """

    def testV0039JobUpdateResponse(self):
        """Test V0039JobUpdateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()