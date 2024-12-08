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

from slurm_client.models.v0040_qos_limits_max_jobs_active_jobs_per import V0040QosLimitsMaxJobsActiveJobsPer

class TestV0040QosLimitsMaxJobsActiveJobsPer(unittest.TestCase):
    """V0040QosLimitsMaxJobsActiveJobsPer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040QosLimitsMaxJobsActiveJobsPer:
        """Test V0040QosLimitsMaxJobsActiveJobsPer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040QosLimitsMaxJobsActiveJobsPer`
        """
        model = V0040QosLimitsMaxJobsActiveJobsPer()
        if include_optional:
            return V0040QosLimitsMaxJobsActiveJobsPer(
                account = slurm_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                user = slurm_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0040QosLimitsMaxJobsActiveJobsPer(
        )
        """

    def testV0040QosLimitsMaxJobsActiveJobsPer(self):
        """Test V0040QosLimitsMaxJobsActiveJobsPer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
