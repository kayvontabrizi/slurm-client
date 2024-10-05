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

from openapi_client.models.v0039_qos_limits_max_jobs_active_jobs_per import V0039QosLimitsMaxJobsActiveJobsPer

class TestV0039QosLimitsMaxJobsActiveJobsPer(unittest.TestCase):
    """V0039QosLimitsMaxJobsActiveJobsPer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039QosLimitsMaxJobsActiveJobsPer:
        """Test V0039QosLimitsMaxJobsActiveJobsPer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039QosLimitsMaxJobsActiveJobsPer`
        """
        model = V0039QosLimitsMaxJobsActiveJobsPer()
        if include_optional:
            return V0039QosLimitsMaxJobsActiveJobsPer(
                account = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                user = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0039QosLimitsMaxJobsActiveJobsPer(
        )
        """

    def testV0039QosLimitsMaxJobsActiveJobsPer(self):
        """Test V0039QosLimitsMaxJobsActiveJobsPer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
