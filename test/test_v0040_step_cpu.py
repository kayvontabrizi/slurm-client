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

from slurm_client.models.v0040_step_cpu import V0040StepCPU

class TestV0040StepCPU(unittest.TestCase):
    """V0040StepCPU unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040StepCPU:
        """Test V0040StepCPU
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040StepCPU`
        """
        model = V0040StepCPU()
        if include_optional:
            return V0040StepCPU(
                requested_frequency = slurm_client.models.v0_0_40_step_cpu_requested_frequency.v0_0_40_step_CPU_requested_frequency(
                    min = slurm_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    max = slurm_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                governor = ''
            )
        else:
            return V0040StepCPU(
        )
        """

    def testV0040StepCPU(self):
        """Test V0040StepCPU"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
