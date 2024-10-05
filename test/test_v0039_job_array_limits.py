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

from openapi_client.models.v0039_job_array_limits import V0039JobArrayLimits

class TestV0039JobArrayLimits(unittest.TestCase):
    """V0039JobArrayLimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039JobArrayLimits:
        """Test V0039JobArrayLimits
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039JobArrayLimits`
        """
        model = V0039JobArrayLimits()
        if include_optional:
            return V0039JobArrayLimits(
                max = openapi_client.models.v0_0_39_job_array_limits_max.v0_0_39_job_array_limits_max(
                    running = openapi_client.models.v0_0_39_job_array_limits_max_running.v0_0_39_job_array_limits_max_running(
                        tasks = 56, ), )
            )
        else:
            return V0039JobArrayLimits(
        )
        """

    def testV0039JobArrayLimits(self):
        """Test V0039JobArrayLimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
