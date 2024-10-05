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

from openapi_client.models.v0039_qos_limits_max_wall_clock import V0039QosLimitsMaxWallClock

class TestV0039QosLimitsMaxWallClock(unittest.TestCase):
    """V0039QosLimitsMaxWallClock unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039QosLimitsMaxWallClock:
        """Test V0039QosLimitsMaxWallClock
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039QosLimitsMaxWallClock`
        """
        model = V0039QosLimitsMaxWallClock()
        if include_optional:
            return V0039QosLimitsMaxWallClock(
                per = openapi_client.models.v0_0_39_qos_limits_max_wall_clock_per.v0_0_39_qos_limits_max_wall_clock_per(
                    qos = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    job = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), )
            )
        else:
            return V0039QosLimitsMaxWallClock(
        )
        """

    def testV0039QosLimitsMaxWallClock(self):
        """Test V0039QosLimitsMaxWallClock"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
