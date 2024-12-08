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

from slurm_client.models.v0042_job_info import V0042JobInfo

class TestV0042JobInfo(unittest.TestCase):
    """V0042JobInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042JobInfo:
        """Test V0042JobInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042JobInfo`
        """
        model = V0042JobInfo()
        if include_optional:
            return V0042JobInfo(
                account = '',
                accrue_time = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                admin_comment = '',
                allocating_node = '',
                array_job_id = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                array_task_id = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                array_max_tasks = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                array_task_string = '',
                association_id = 56,
                batch_features = '',
                batch_flag = True,
                batch_host = '',
                flags = [
                    'KILL_INVALID_DEPENDENCY'
                    ],
                burst_buffer = '',
                burst_buffer_state = '',
                cluster = '',
                cluster_features = '',
                command = '',
                comment = '',
                container = '',
                container_id = '',
                contiguous = True,
                core_spec = 56,
                thread_spec = 56,
                cores_per_socket = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                billable_tres = slurm_client.models.v0/0/42_float64_no_val_struct.v0.0.42_float64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 1.337, ),
                cpus_per_task = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                cpu_frequency_minimum = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                cpu_frequency_maximum = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                cpu_frequency_governor = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                cpus_per_tres = '',
                cron = '',
                deadline = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                delay_boot = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                dependency = '',
                derived_exit_code = slurm_client.models.v0/0/42_process_exit_code_verbose.v0.0.42_process_exit_code_verbose(
                    status = [
                        'INVALID'
                        ], 
                    return_code = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    signal = slurm_client.models.v0_0_42_process_exit_code_verbose_signal.v0_0_42_process_exit_code_verbose_signal(
                        id = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        name = '', ), ),
                eligible_time = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                end_time = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                excluded_nodes = '',
                exit_code = slurm_client.models.v0/0/42_process_exit_code_verbose.v0.0.42_process_exit_code_verbose(
                    status = [
                        'INVALID'
                        ], 
                    return_code = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    signal = slurm_client.models.v0_0_42_process_exit_code_verbose_signal.v0_0_42_process_exit_code_verbose_signal(
                        id = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        name = '', ), ),
                extra = '',
                failed_node = '',
                features = '',
                federation_origin = '',
                federation_siblings_active = '',
                federation_siblings_viable = '',
                gres_detail = [
                    ''
                    ],
                group_id = 56,
                group_name = '',
                het_job_id = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                het_job_id_set = '',
                het_job_offset = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                job_id = 56,
                job_resources = slurm_client.models.v0/0/42_job_res.v0.0.42_job_res(
                    select_type = [
                        'CPU'
                        ], 
                    nodes = slurm_client.models.v0_0_42_job_res_nodes.v0_0_42_job_res_nodes(
                        count = 56, 
                        list = '', 
                        whole = True, 
                        allocation = [
                            slurm_client.models.v0/0/42_job_res_node.v0.0.42_job_res_node(
                                index = 56, 
                                name = '', 
                                cpus = slurm_client.models.v0_0_42_job_res_node_cpus.v0_0_42_job_res_node_cpus(
                                    count = 56, 
                                    used = 56, ), 
                                memory = slurm_client.models.v0_0_42_job_res_node_memory.v0_0_42_job_res_node_memory(
                                    used = 56, 
                                    allocated = 56, ), 
                                sockets = [
                                    slurm_client.models.v0/0/42_job_res_socket.v0.0.42_job_res_socket(
                                        index = 56, 
                                        cores = [
                                            slurm_client.models.v0/0/42_job_res_core.v0.0.42_job_res_core(
                                                index = 56, 
                                                status = [
                                                    'INVALID'
                                                    ], )
                                            ], )
                                    ], )
                            ], ), 
                    cpus = 56, 
                    threads_per_core = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                job_size_str = [
                    ''
                    ],
                job_state = [
                    'PENDING'
                    ],
                last_sched_evaluation = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                licenses = '',
                mail_type = [
                    'BEGIN'
                    ],
                mail_user = '',
                max_cpus = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                max_nodes = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                mcs_label = '',
                memory_per_tres = '',
                name = '',
                network = '',
                nodes = '',
                nice = 56,
                tasks_per_core = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                tasks_per_tres = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                tasks_per_node = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                tasks_per_socket = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                tasks_per_board = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                cpus = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                node_count = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                tasks = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                partition = '',
                prefer = '',
                memory_per_cpu = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                memory_per_node = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                minimum_cpus_per_node = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                minimum_tmp_disk_per_node = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                power = slurm_client.models.v0_0_42_job_info_power.v0_0_42_job_info_power(
                    flags = [
                        null
                        ], ),
                preempt_time = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                preemptable_time = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                pre_sus_time = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                hold = True,
                priority = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                priority_by_partition = [
                    slurm_client.models.v0/0/42_part_prio.v0.0.42_part_prio(
                        partition = '', 
                        priority = 56, )
                    ],
                profile = [
                    'NOT_SET'
                    ],
                qos = '',
                reboot = True,
                required_nodes = '',
                required_switches = 56,
                requeue = True,
                resize_time = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                restart_cnt = 56,
                resv_name = '',
                scheduled_nodes = '',
                selinux_context = '',
                shared = [
                    'none'
                    ],
                sockets_per_board = 56,
                sockets_per_node = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                start_time = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                state_description = '',
                state_reason = '',
                standard_error = '',
                standard_input = '',
                standard_output = '',
                submit_time = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                suspend_time = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                system_comment = '',
                time_limit = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                time_minimum = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                threads_per_core = slurm_client.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                tres_bind = '',
                tres_freq = '',
                tres_per_job = '',
                tres_per_node = '',
                tres_per_socket = '',
                tres_per_task = '',
                tres_req_str = '',
                tres_alloc_str = '',
                user_id = 56,
                user_name = '',
                maximum_switch_wait_time = 56,
                wckey = '',
                current_working_directory = ''
            )
        else:
            return V0042JobInfo(
        )
        """

    def testV0042JobInfo(self):
        """Test V0042JobInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
