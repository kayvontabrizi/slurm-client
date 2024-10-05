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

from slurm_client.models.v0039_stats_user import V0039StatsUser

class TestV0039StatsUser(unittest.TestCase):
    """V0039StatsUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039StatsUser:
        """Test V0039StatsUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039StatsUser`
        """
        model = V0039StatsUser()
        if include_optional:
            return V0039StatsUser(
                user = '',
                count = 56,
                time = slurm_client.models.v0_0_39_stats_rpc_time.v0_0_39_stats_rpc_time(
                    average = 56, 
                    total = 56, )
            )
        else:
            return V0039StatsUser(
        )
        """

    def testV0039StatsUser(self):
        """Test V0039StatsUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
