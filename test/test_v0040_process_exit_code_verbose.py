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

from openapi_client.models.v0040_process_exit_code_verbose import V0040ProcessExitCodeVerbose

class TestV0040ProcessExitCodeVerbose(unittest.TestCase):
    """V0040ProcessExitCodeVerbose unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040ProcessExitCodeVerbose:
        """Test V0040ProcessExitCodeVerbose
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040ProcessExitCodeVerbose`
        """
        model = V0040ProcessExitCodeVerbose()
        if include_optional:
            return V0040ProcessExitCodeVerbose(
                status = [
                    'INVALID'
                    ],
                return_code = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                signal = openapi_client.models.v0_0_40_process_exit_code_verbose_signal.v0_0_40_process_exit_code_verbose_signal(
                    id = openapi_client.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    name = '', )
            )
        else:
            return V0040ProcessExitCodeVerbose(
        )
        """

    def testV0040ProcessExitCodeVerbose(self):
        """Test V0040ProcessExitCodeVerbose"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()