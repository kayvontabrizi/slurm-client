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

from slurm_client.models.v0039_job_required import V0039JobRequired

class TestV0039JobRequired(unittest.TestCase):
    """V0039JobRequired unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039JobRequired:
        """Test V0039JobRequired
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039JobRequired`
        """
        model = V0039JobRequired()
        if include_optional:
            return V0039JobRequired(
                cpus = 56,
                memory_per_cpu = slurm_client.models.v0/0/39_uint64_no_val.v0.0.39_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                memory_per_node = slurm_client.models.v0/0/39_uint64_no_val.v0.0.39_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                memory = 56
            )
        else:
            return V0039JobRequired(
        )
        """

    def testV0039JobRequired(self):
        """Test V0039JobRequired"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
