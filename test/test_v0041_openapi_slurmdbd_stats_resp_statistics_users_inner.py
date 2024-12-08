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

from slurm_client.models.v0041_openapi_slurmdbd_stats_resp_statistics_users_inner import V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner

class TestV0041OpenapiSlurmdbdStatsRespStatisticsUsersInner(unittest.TestCase):
    """V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner:
        """Test V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner`
        """
        model = V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner()
        if include_optional:
            return V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner(
                user = '',
                count = 56,
                time = slurm_client.models.v0_0_42_stats_rpc_time.v0_0_42_stats_rpc_time(
                    average = 56, 
                    total = 56, )
            )
        else:
            return V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner(
        )
        """

    def testV0041OpenapiSlurmdbdStatsRespStatisticsUsersInner(self):
        """Test V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()