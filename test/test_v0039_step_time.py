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

from slurm_client.models.v0039_step_time import V0039StepTime

class TestV0039StepTime(unittest.TestCase):
    """V0039StepTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039StepTime:
        """Test V0039StepTime
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039StepTime`
        """
        model = V0039StepTime()
        if include_optional:
            return V0039StepTime(
                elapsed = 56,
                end = 56,
                start = 56,
                suspended = 56,
                system = slurm_client.models.v0_0_39_step_time_system.v0_0_39_step_time_system(
                    seconds = 56, 
                    microseconds = 56, ),
                total = slurm_client.models.v0_0_39_step_time_system.v0_0_39_step_time_system(
                    seconds = 56, 
                    microseconds = 56, ),
                user = slurm_client.models.v0_0_39_step_time_system.v0_0_39_step_time_system(
                    seconds = 56, 
                    microseconds = 56, )
            )
        else:
            return V0039StepTime(
        )
        """

    def testV0039StepTime(self):
        """Test V0039StepTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
