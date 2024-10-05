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

from openapi_client.models.v0041_openapi_diag_resp_statistics import V0041OpenapiDiagRespStatistics

class TestV0041OpenapiDiagRespStatistics(unittest.TestCase):
    """V0041OpenapiDiagRespStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiDiagRespStatistics:
        """Test V0041OpenapiDiagRespStatistics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiDiagRespStatistics`
        """
        model = V0041OpenapiDiagRespStatistics()
        if include_optional:
            return V0041OpenapiDiagRespStatistics(
                parts_packed = 56,
                req_time = openapi_client.models.v0_0_41_openapi_diag_resp_statistics_req_time.v0_0_41_openapi_diag_resp_statistics_req_time(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                req_time_start = openapi_client.models.v0_0_41_openapi_diag_resp_statistics_req_time_start.v0_0_41_openapi_diag_resp_statistics_req_time_start(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                server_thread_count = 56,
                agent_queue_size = 56,
                agent_count = 56,
                agent_thread_count = 56,
                dbd_agent_queue_size = 56,
                gettimeofday_latency = 56,
                schedule_cycle_max = 56,
                schedule_cycle_last = 56,
                schedule_cycle_sum = 56,
                schedule_cycle_total = 56,
                schedule_cycle_mean = 56,
                schedule_cycle_mean_depth = 56,
                schedule_cycle_per_minute = 56,
                schedule_cycle_depth = 56,
                schedule_exit = openapi_client.models.v0_0_41_openapi_diag_resp_statistics_schedule_exit.v0_0_41_openapi_diag_resp_statistics_schedule_exit(
                    end_job_queue = 56, 
                    default_queue_depth = 56, 
                    max_job_start = 56, 
                    max_rpc_cnt = 56, 
                    max_sched_time = 56, 
                    licenses = 56, ),
                schedule_queue_length = 56,
                jobs_submitted = 56,
                jobs_started = 56,
                jobs_completed = 56,
                jobs_canceled = 56,
                jobs_failed = 56,
                jobs_pending = 56,
                jobs_running = 56,
                job_states_ts = openapi_client.models.v0_0_41_openapi_diag_resp_statistics_job_states_ts.v0_0_41_openapi_diag_resp_statistics_job_states_ts(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                bf_backfilled_jobs = 56,
                bf_last_backfilled_jobs = 56,
                bf_backfilled_het_jobs = 56,
                bf_cycle_counter = 56,
                bf_cycle_mean = 56,
                bf_depth_mean = 56,
                bf_depth_mean_try = 56,
                bf_cycle_sum = 56,
                bf_cycle_last = 56,
                bf_cycle_max = 56,
                bf_exit = openapi_client.models.v0_0_41_openapi_diag_resp_statistics_bf_exit.v0_0_41_openapi_diag_resp_statistics_bf_exit(
                    end_job_queue = 56, 
                    bf_max_job_start = 56, 
                    bf_max_job_test = 56, 
                    bf_max_time = 56, 
                    bf_node_space_size = 56, 
                    state_changed = 56, ),
                bf_last_depth = 56,
                bf_last_depth_try = 56,
                bf_depth_sum = 56,
                bf_depth_try_sum = 56,
                bf_queue_len = 56,
                bf_queue_len_mean = 56,
                bf_queue_len_sum = 56,
                bf_table_size = 56,
                bf_table_size_sum = 56,
                bf_table_size_mean = 56,
                bf_when_last_cycle = openapi_client.models.v0_0_41_openapi_diag_resp_statistics_bf_when_last_cycle.v0_0_41_openapi_diag_resp_statistics_bf_when_last_cycle(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                bf_active = True,
                rpcs_by_message_type = [
                    openapi_client.models.v0_0_41_openapi_diag_resp_statistics_rpcs_by_message_type_inner.v0_0_41_openapi_diag_resp_statistics_rpcs_by_message_type_inner(
                        type_id = 56, 
                        message_type = '', 
                        count = 56, 
                        queued = 56, 
                        dropped = 56, 
                        cycle_last = 56, 
                        cycle_max = 56, 
                        total_time = 56, 
                        average_time = openapi_client.models.v0_0_41_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time.v0_0_41_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time(
                            set = True, 
                            infinite = True, 
                            number = 56, ), )
                    ],
                rpcs_by_user = [
                    openapi_client.models.v0_0_41_openapi_diag_resp_statistics_rpcs_by_user_inner.v0_0_41_openapi_diag_resp_statistics_rpcs_by_user_inner(
                        user_id = 56, 
                        user = '', 
                        count = 56, 
                        total_time = 56, 
                        average_time = openapi_client.models.v0_0_41_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time.v0_0_41_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time(
                            set = True, 
                            infinite = True, 
                            number = 56, ), )
                    ],
                pending_rpcs = [
                    openapi_client.models.v0_0_41_openapi_diag_resp_statistics_pending_rpcs_inner.v0_0_41_openapi_diag_resp_statistics_pending_rpcs_inner(
                        type_id = 56, 
                        message_type = '', 
                        count = 56, )
                    ],
                pending_rpcs_by_hostlist = [
                    openapi_client.models.v0_0_41_openapi_diag_resp_statistics_pending_rpcs_by_hostlist_inner.v0_0_41_openapi_diag_resp_statistics_pending_rpcs_by_hostlist_inner(
                        type_id = 56, 
                        message_type = '', 
                        count = [
                            ''
                            ], )
                    ]
            )
        else:
            return V0041OpenapiDiagRespStatistics(
        )
        """

    def testV0041OpenapiDiagRespStatistics(self):
        """Test V0041OpenapiDiagRespStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
