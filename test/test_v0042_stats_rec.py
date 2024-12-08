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

from slurm_client.models.v0042_stats_rec import V0042StatsRec

class TestV0042StatsRec(unittest.TestCase):
    """V0042StatsRec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042StatsRec:
        """Test V0042StatsRec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042StatsRec`
        """
        model = V0042StatsRec()
        if include_optional:
            return V0042StatsRec(
                time_start = 56,
                rollups = slurm_client.models.v0/0/42_rollup_stats.v0.0.42_rollup_stats(
                    hourly = slurm_client.models.v0_0_42_rollup_stats_hourly.v0_0_42_rollup_stats_hourly(
                        count = 56, 
                        last_run = 56, 
                        duration = slurm_client.models.v0_0_42_rollup_stats_hourly_duration.v0_0_42_rollup_stats_hourly_duration(
                            last = 56, 
                            max = 56, 
                            time = 56, ), ), 
                    daily = slurm_client.models.v0_0_42_rollup_stats_daily.v0_0_42_rollup_stats_daily(
                        count = 56, 
                        last_run = 56, ), 
                    monthly = slurm_client.models.v0_0_42_rollup_stats_monthly.v0_0_42_rollup_stats_monthly(
                        count = 56, 
                        last_run = 56, ), ),
                rpcs = [
                    slurm_client.models.v0/0/42_stats_rpc.v0.0.42_stats_rpc(
                        rpc = '', 
                        count = 56, 
                        time = slurm_client.models.v0_0_42_stats_rpc_time.v0_0_42_stats_rpc_time(
                            average = 56, 
                            total = 56, ), )
                    ],
                users = [
                    slurm_client.models.v0/0/42_stats_user.v0.0.42_stats_user(
                        user = '', 
                        count = 56, 
                        time = slurm_client.models.v0_0_42_stats_rpc_time.v0_0_42_stats_rpc_time(
                            average = 56, 
                            total = 56, ), )
                    ]
            )
        else:
            return V0042StatsRec(
        )
        """

    def testV0042StatsRec(self):
        """Test V0042StatsRec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
