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

from openapi_client.models.v0039_stats_msg import V0039StatsMsg

class TestV0039StatsMsg(unittest.TestCase):
    """V0039StatsMsg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039StatsMsg:
        """Test V0039StatsMsg
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039StatsMsg`
        """
        model = V0039StatsMsg()
        if include_optional:
            return V0039StatsMsg(
                parts_packed = 56,
                req_time = 56,
                req_time_start = 56,
                server_thread_count = 56,
                agent_queue_size = 56,
                agent_count = 56,
                agent_thread_count = 56,
                dbd_agent_queue_size = 56,
                gettimeofday_latency = 56,
                schedule_cycle_max = 56,
                schedule_cycle_last = 56,
                schedule_cycle_total = 56,
                schedule_cycle_mean = 56,
                schedule_cycle_mean_depth = 56,
                schedule_cycle_per_minute = 56,
                schedule_queue_length = 56,
                jobs_submitted = 56,
                jobs_started = 56,
                jobs_completed = 56,
                jobs_canceled = 56,
                jobs_failed = 56,
                jobs_pending = 56,
                jobs_running = 56,
                job_states_ts = 56,
                bf_backfilled_jobs = 56,
                bf_last_backfilled_jobs = 56,
                bf_backfilled_het_jobs = 56,
                bf_cycle_counter = 56,
                bf_cycle_mean = 56,
                bf_depth_mean = 56,
                bf_depth_mean_try = 56,
                bf_cycle_sum = 56,
                bf_cycle_last = 56,
                bf_last_depth = 56,
                bf_last_depth_try = 56,
                bf_depth_sum = 56,
                bf_depth_try_sum = 56,
                bf_queue_len = 56,
                bf_queue_len_mean = 56,
                bf_queue_len_sum = 56,
                bf_table_size = 56,
                bf_table_size_mean = 56,
                bf_when_last_cycle = 56,
                bf_active = True,
                rpcs_by_message_type = [
                    openapi_client.models.v0_0_40_stats_msg_rpcs_by_type_inner.v0_0_40_stats_msg_rpcs_by_type_inner(
                        message_type = '', 
                        type_id = 56, 
                        count = 56, 
                        average_time = 56, 
                        total_time = 56, )
                    ],
                rpcs_by_user = [
                    openapi_client.models.v0_0_40_stats_msg_rpcs_by_user_inner.v0_0_40_stats_msg_rpcs_by_user_inner(
                        user = '', 
                        user_id = 56, 
                        count = 56, 
                        average_time = 56, 
                        total_time = 56, )
                    ]
            )
        else:
            return V0039StatsMsg(
        )
        """

    def testV0039StatsMsg(self):
        """Test V0039StatsMsg"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
