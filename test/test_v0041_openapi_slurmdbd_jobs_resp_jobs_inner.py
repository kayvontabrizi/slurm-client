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

from slurm_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner import V0041OpenapiSlurmdbdJobsRespJobsInner

class TestV0041OpenapiSlurmdbdJobsRespJobsInner(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInner:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInner`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInner()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInner(
                account = '',
                comment = slurm_client.models.v0_0_42_job_comment.v0_0_42_job_comment(
                    administrator = '', 
                    job = '', 
                    system = '', ),
                allocation_nodes = 56,
                array = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array(
                    job_id = 56, 
                    limits = slurm_client.models.v0_0_42_job_array_limits.v0_0_42_job_array_limits(
                        max = slurm_client.models.v0_0_42_job_array_limits_max.v0_0_42_job_array_limits_max(
                            running = slurm_client.models.v0_0_42_job_array_limits_max_running.v0_0_42_job_array_limits_max_running(
                                tasks = 56, ), ), ), 
                    task_id = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_array_task_id.v0_0_41_openapi_job_info_resp_jobs_inner_array_task_id(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    task = '', ),
                association = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_association.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_association(
                    account = '', 
                    cluster = '', 
                    partition = '', 
                    user = '', 
                    id = 56, ),
                block = '',
                cluster = '',
                constraints = '',
                container = '',
                derived_exit_code = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code(
                    status = [
                        'INVALID'
                        ], 
                    return_code = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_return_code.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_return_code(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    signal = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal(
                        id = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal_id.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal_id(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        name = '', ), ),
                time = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time(
                    elapsed = 56, 
                    eligible = 56, 
                    end = 56, 
                    planned = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    start = 56, 
                    submission = 56, 
                    suspended = 56, 
                    system = slurm_client.models.v0_0_42_job_time_system.v0_0_42_job_time_system(
                        seconds = 56, 
                        microseconds = 56, ), 
                    limit = slurm_client.models.v0_0_41_job_desc_msg_time_limit.v0_0_41_job_desc_msg_time_limit(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    total = slurm_client.models.v0_0_42_job_time_total.v0_0_42_job_time_total(
                        seconds = 56, 
                        microseconds = 56, ), 
                    user = slurm_client.models.v0_0_42_job_time_user.v0_0_42_job_time_user(
                        seconds = 56, 
                        microseconds = 56, ), ),
                exit_code = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_exit_code.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_exit_code(
                    status = [
                        'INVALID'
                        ], 
                    return_code = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_return_code.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_return_code(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    signal = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal(
                        id = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal_id.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal_id(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        name = '', ), ),
                extra = '',
                failed_node = '',
                flags = [
                    'NONE'
                    ],
                group = '',
                het = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_het.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_het(
                    job_id = 56, 
                    job_offset = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_het_job_offset.v0_0_41_openapi_job_info_resp_jobs_inner_het_job_offset(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                job_id = 56,
                name = '',
                licenses = '',
                mcs = slurm_client.models.v0_0_42_job_mcs.v0_0_42_job_mcs(
                    label = '', ),
                nodes = '',
                partition = '',
                hold = True,
                priority = slurm_client.models.v0_0_41_job_desc_msg_priority.v0_0_41_job_desc_msg_priority(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                qos = '',
                required = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required(
                    cpus = 56, 
                    memory_per_cpu = slurm_client.models.v0_0_41_job_desc_msg_memory_per_cpu.v0_0_41_job_desc_msg_memory_per_cpu(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    memory_per_node = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_memory_per_node.v0_0_41_openapi_job_info_resp_jobs_inner_memory_per_node(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                kill_request_user = '',
                reservation = slurm_client.models.v0_0_42_job_reservation.v0_0_42_job_reservation(
                    id = 56, 
                    name = '', ),
                script = '',
                stdin_expanded = '',
                stdout_expanded = '',
                stderr_expanded = '',
                stdout = '',
                stderr = '',
                stdin = '',
                state = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_state.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_state(
                    current = [
                        'PENDING'
                        ], 
                    reason = '', ),
                steps = [
                    slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner(
                        time = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time(
                            elapsed = 56, 
                            end = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_end.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_end(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            start = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_start.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_start(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            suspended = 56, 
                            system = slurm_client.models.v0_0_42_step_time_system.v0_0_42_step_time_system(
                                seconds = 56, 
                                microseconds = 56, ), 
                            total = slurm_client.models.v0_0_42_step_time_total.v0_0_42_step_time_total(
                                seconds = 56, 
                                microseconds = 56, ), 
                            user = slurm_client.models.v0_0_42_step_time_user.v0_0_42_step_time_user(
                                seconds = 56, 
                                microseconds = 56, ), ), 
                        exit_code = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_exit_code.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_exit_code(
                            status = [
                                'INVALID'
                                ], 
                            return_code = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_return_code.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_return_code(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            signal = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal(
                                id = slurm_client.models.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal_id.v0_0_41_openapi_job_info_resp_jobs_inner_derived_exit_code_signal_id(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), 
                                name = '', ), ), 
                        nodes = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes(
                            count = 56, 
                            range = '', 
                            list = [
                                ''
                                ], ), 
                        tasks = slurm_client.models.v0_0_42_step_tasks.v0_0_42_step_tasks(
                            count = 56, ), 
                        pid = '', 
                        cpu = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU(
                            requested_frequency = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU_requested_frequency(
                                min = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency_min.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU_requested_frequency_min(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), 
                                max = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency_max.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU_requested_frequency_max(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), ), 
                            governor = '', ), 
                        kill_request_user = '', 
                        state = [
                            'PENDING'
                            ], 
                        statistics = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics(
                            energy = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy(
                                consumed = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy_consumed.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy_consumed(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), ), ), 
                        step = slurm_client.models.v0_0_42_step_step.v0_0_42_step_step(
                            name = '', ), 
                        task = slurm_client.models.v0_0_42_step_task.v0_0_42_step_task(
                            distribution = '', ), 
                        tres = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres(
                            requested = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested(
                                average = [
                                    slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                        type = '', 
                                        name = '', 
                                        count = 56, )
                                    ], ), 
                            allocated = [
                                slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                    type = '', 
                                    name = '', 
                                    count = 56, )
                                ], ), )
                    ],
                submit_line = '',
                tres = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_tres.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_tres(
                    allocated = [
                        slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], 
                    requested = [
                        slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], ),
                used_gres = '',
                user = '',
                wckey = slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_wckey.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_wckey(
                    wckey = '', 
                    flags = [
                        'ASSIGNED_DEFAULT'
                        ], ),
                working_directory = ''
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInner(
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInner(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
