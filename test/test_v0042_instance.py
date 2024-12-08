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

from slurm_client.models.v0042_instance import V0042Instance

class TestV0042Instance(unittest.TestCase):
    """V0042Instance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042Instance:
        """Test V0042Instance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042Instance`
        """
        model = V0042Instance()
        if include_optional:
            return V0042Instance(
                cluster = '',
                extra = '',
                instance_id = '',
                instance_type = '',
                node_name = '',
                time = slurm_client.models.v0_0_42_instance_time.v0_0_42_instance_time(
                    time_end = 56, 
                    time_start = 56, )
            )
        else:
            return V0042Instance(
        )
        """

    def testV0042Instance(self):
        """Test V0042Instance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
