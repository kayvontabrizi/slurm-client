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

from slurm_client.models.v0042_job_het import V0042JobHet

class TestV0042JobHet(unittest.TestCase):
    """V0042JobHet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042JobHet:
        """Test V0042JobHet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042JobHet`
        """
        model = V0042JobHet()
        if include_optional:
            return V0042JobHet(
                job_id = 56,
                job_offset = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0042JobHet(
        )
        """

    def testV0042JobHet(self):
        """Test V0042JobHet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
