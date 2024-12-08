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

from slurm_client.models.v0042_step_tres_requested import V0042StepTresRequested

class TestV0042StepTresRequested(unittest.TestCase):
    """V0042StepTresRequested unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042StepTresRequested:
        """Test V0042StepTresRequested
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042StepTresRequested`
        """
        model = V0042StepTresRequested()
        if include_optional:
            return V0042StepTresRequested(
                max = [
                    slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                min = [
                    slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                average = [
                    slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                total = [
                    slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return V0042StepTresRequested(
        )
        """

    def testV0042StepTresRequested(self):
        """Test V0042StepTresRequested"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
