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

from slurm_client.models.v0042_openapi_slurmdbd_jobs_resp import V0042OpenapiSlurmdbdJobsResp

class TestV0042OpenapiSlurmdbdJobsResp(unittest.TestCase):
    """V0042OpenapiSlurmdbdJobsResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042OpenapiSlurmdbdJobsResp:
        """Test V0042OpenapiSlurmdbdJobsResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042OpenapiSlurmdbdJobsResp`
        """
        model = V0042OpenapiSlurmdbdJobsResp()
        if include_optional:
            return V0042OpenapiSlurmdbdJobsResp(
                jobs = [
                    slurm_client.models.v0/0/42_job.v0.0.42_job(
                        account = '', 
                        comment = slurm_client.models.v0_0_42_job_comment.v0_0_42_job_comment(
                            administrator = '', 
                            job = '', 
                            system = '', ), 
                        allocation_nodes = 56, 
                        array = slurm_client.models.v0_0_42_job_array.v0_0_42_job_array(
                            job_id = 56, 
                            limits = slurm_client.models.v0_0_42_job_array_limits.v0_0_42_job_array_limits(
                                max = slurm_client.models.v0_0_42_job_array_limits_max.v0_0_42_job_array_limits_max(
                                    running = slurm_client.models.v0_0_42_job_array_limits_max_running.v0_0_42_job_array_limits_max_running(
                                        tasks = 56, ), ), ), 
                            task_id = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            task = '', ), 
                        association = slurm_client.models.v0/0/42_assoc_short.v0.0.42_assoc_short(
                            account = '', 
                            cluster = '', 
                            partition = '', 
                            user = '', 
                            id = 56, ), 
                        block = '', 
                        cluster = '', 
                        constraints = '', 
                        container = '', 
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
                        time = slurm_client.models.v0_0_42_job_time.v0_0_42_job_time(
                            elapsed = 56, 
                            eligible = 56, 
                            end = 56, 
                            planned = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            start = 56, 
                            submission = 56, 
                            suspended = 56, 
                            system = slurm_client.models.v0_0_42_job_time_system.v0_0_42_job_time_system(
                                seconds = 56, 
                                microseconds = 56, ), 
                            limit = , 
                            total = slurm_client.models.v0_0_42_job_time_total.v0_0_42_job_time_total(
                                seconds = 56, 
                                microseconds = 56, ), 
                            user = slurm_client.models.v0_0_42_job_time_user.v0_0_42_job_time_user(
                                seconds = 56, 
                                microseconds = 56, ), ), 
                        exit_code = slurm_client.models.v0/0/42_process_exit_code_verbose.v0.0.42_process_exit_code_verbose(
                            status = [
                                'INVALID'
                                ], ), 
                        extra = '', 
                        failed_node = '', 
                        flags = [
                            'NONE'
                            ], 
                        group = '', 
                        het = slurm_client.models.v0_0_42_job_het.v0_0_42_job_het(
                            job_id = 56, 
                            job_offset = , ), 
                        job_id = 56, 
                        name = '', 
                        licenses = '', 
                        mcs = slurm_client.models.v0_0_42_job_mcs.v0_0_42_job_mcs(
                            label = '', ), 
                        nodes = '', 
                        partition = '', 
                        hold = True, 
                        priority = , 
                        qos = '', 
                        qosreq = '', 
                        required = slurm_client.models.v0_0_42_job_required.v0_0_42_job_required(
                            cpus = 56, 
                            memory_per_cpu = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            memory_per_node = , ), 
                        kill_request_user = '', 
                        restart_cnt = 56, 
                        reservation = slurm_client.models.v0_0_42_job_reservation.v0_0_42_job_reservation(
                            name = '', ), 
                        script = '', 
                        stdin_expanded = '', 
                        stdout_expanded = '', 
                        stderr_expanded = '', 
                        stdout = '', 
                        stderr = '', 
                        stdin = '', 
                        state = slurm_client.models.v0_0_42_job_state.v0_0_42_job_state(
                            current = [
                                'PENDING'
                                ], 
                            reason = '', ), 
                        steps = [
                            slurm_client.models.v0/0/42_step.v0.0.42_step(
                                nodes = slurm_client.models.v0_0_42_step_nodes.v0_0_42_step_nodes(
                                    count = 56, 
                                    range = '', 
                                    list = [
                                        ''
                                        ], ), 
                                tasks = slurm_client.models.v0_0_42_step_tasks.v0_0_42_step_tasks(
                                    count = 56, ), 
                                pid = '', 
                                cpu = slurm_client.models.v0_0_42_step_cpu.v0_0_42_step_CPU(
                                    requested_frequency = slurm_client.models.v0_0_42_step_cpu_requested_frequency.v0_0_42_step_CPU_requested_frequency(
                                        min = , ), 
                                    governor = '', ), 
                                kill_request_user = '', 
                                statistics = slurm_client.models.v0_0_42_step_statistics.v0_0_42_step_statistics(
                                    energy = slurm_client.models.v0_0_42_step_statistics_energy.v0_0_42_step_statistics_energy(
                                        consumed = , ), ), 
                                step = slurm_client.models.v0_0_42_step_step.v0_0_42_step_step(
                                    name = '', ), 
                                task = slurm_client.models.v0_0_42_step_task.v0_0_42_step_task(
                                    distribution = '', ), 
                                tres = slurm_client.models.v0_0_42_step_tres.v0_0_42_step_tres(
                                    requested = slurm_client.models.v0_0_42_step_tres_requested.v0_0_42_step_tres_requested(
                                        average = [
                                            slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                                                type = '', 
                                                name = '', 
                                                count = 56, )
                                            ], ), 
                                    allocated = [
                                        slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                                            type = '', 
                                            name = '', 
                                            count = 56, )
                                        ], ), )
                            ], 
                        submit_line = '', 
                        tres = slurm_client.models.v0_0_42_job_tres.v0_0_42_job_tres(), 
                        used_gres = '', 
                        user = '', 
                        wckey = slurm_client.models.v0/0/42_wckey_tag_struct.v0.0.42_wckey_tag_struct(
                            wckey = '', 
                            flags = [
                                'ASSIGNED_DEFAULT'
                                ], ), 
                        working_directory = '', )
                    ],
                meta = slurm_client.models.v0/0/42_openapi_meta.v0.0.42_openapi_meta(
                    plugin = slurm_client.models.v0_0_42_openapi_meta_plugin.v0_0_42_openapi_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = slurm_client.models.v0_0_42_openapi_meta_client.v0_0_42_openapi_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = slurm_client.models.v0_0_42_openapi_meta_slurm.v0_0_42_openapi_meta_slurm(
                        version = slurm_client.models.v0_0_42_openapi_meta_slurm_version.v0_0_42_openapi_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', 
                        cluster = '', ), ),
                errors = [
                    slurm_client.models.v0/0/42_openapi_error.v0.0.42_openapi_error(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    slurm_client.models.v0/0/42_openapi_warning.v0.0.42_openapi_warning(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0042OpenapiSlurmdbdJobsResp(
                jobs = [
                    slurm_client.models.v0/0/42_job.v0.0.42_job(
                        account = '', 
                        comment = slurm_client.models.v0_0_42_job_comment.v0_0_42_job_comment(
                            administrator = '', 
                            job = '', 
                            system = '', ), 
                        allocation_nodes = 56, 
                        array = slurm_client.models.v0_0_42_job_array.v0_0_42_job_array(
                            job_id = 56, 
                            limits = slurm_client.models.v0_0_42_job_array_limits.v0_0_42_job_array_limits(
                                max = slurm_client.models.v0_0_42_job_array_limits_max.v0_0_42_job_array_limits_max(
                                    running = slurm_client.models.v0_0_42_job_array_limits_max_running.v0_0_42_job_array_limits_max_running(
                                        tasks = 56, ), ), ), 
                            task_id = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            task = '', ), 
                        association = slurm_client.models.v0/0/42_assoc_short.v0.0.42_assoc_short(
                            account = '', 
                            cluster = '', 
                            partition = '', 
                            user = '', 
                            id = 56, ), 
                        block = '', 
                        cluster = '', 
                        constraints = '', 
                        container = '', 
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
                        time = slurm_client.models.v0_0_42_job_time.v0_0_42_job_time(
                            elapsed = 56, 
                            eligible = 56, 
                            end = 56, 
                            planned = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            start = 56, 
                            submission = 56, 
                            suspended = 56, 
                            system = slurm_client.models.v0_0_42_job_time_system.v0_0_42_job_time_system(
                                seconds = 56, 
                                microseconds = 56, ), 
                            limit = , 
                            total = slurm_client.models.v0_0_42_job_time_total.v0_0_42_job_time_total(
                                seconds = 56, 
                                microseconds = 56, ), 
                            user = slurm_client.models.v0_0_42_job_time_user.v0_0_42_job_time_user(
                                seconds = 56, 
                                microseconds = 56, ), ), 
                        exit_code = slurm_client.models.v0/0/42_process_exit_code_verbose.v0.0.42_process_exit_code_verbose(
                            status = [
                                'INVALID'
                                ], ), 
                        extra = '', 
                        failed_node = '', 
                        flags = [
                            'NONE'
                            ], 
                        group = '', 
                        het = slurm_client.models.v0_0_42_job_het.v0_0_42_job_het(
                            job_id = 56, 
                            job_offset = , ), 
                        job_id = 56, 
                        name = '', 
                        licenses = '', 
                        mcs = slurm_client.models.v0_0_42_job_mcs.v0_0_42_job_mcs(
                            label = '', ), 
                        nodes = '', 
                        partition = '', 
                        hold = True, 
                        priority = , 
                        qos = '', 
                        qosreq = '', 
                        required = slurm_client.models.v0_0_42_job_required.v0_0_42_job_required(
                            cpus = 56, 
                            memory_per_cpu = slurm_client.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            memory_per_node = , ), 
                        kill_request_user = '', 
                        restart_cnt = 56, 
                        reservation = slurm_client.models.v0_0_42_job_reservation.v0_0_42_job_reservation(
                            name = '', ), 
                        script = '', 
                        stdin_expanded = '', 
                        stdout_expanded = '', 
                        stderr_expanded = '', 
                        stdout = '', 
                        stderr = '', 
                        stdin = '', 
                        state = slurm_client.models.v0_0_42_job_state.v0_0_42_job_state(
                            current = [
                                'PENDING'
                                ], 
                            reason = '', ), 
                        steps = [
                            slurm_client.models.v0/0/42_step.v0.0.42_step(
                                nodes = slurm_client.models.v0_0_42_step_nodes.v0_0_42_step_nodes(
                                    count = 56, 
                                    range = '', 
                                    list = [
                                        ''
                                        ], ), 
                                tasks = slurm_client.models.v0_0_42_step_tasks.v0_0_42_step_tasks(
                                    count = 56, ), 
                                pid = '', 
                                cpu = slurm_client.models.v0_0_42_step_cpu.v0_0_42_step_CPU(
                                    requested_frequency = slurm_client.models.v0_0_42_step_cpu_requested_frequency.v0_0_42_step_CPU_requested_frequency(
                                        min = , ), 
                                    governor = '', ), 
                                kill_request_user = '', 
                                statistics = slurm_client.models.v0_0_42_step_statistics.v0_0_42_step_statistics(
                                    energy = slurm_client.models.v0_0_42_step_statistics_energy.v0_0_42_step_statistics_energy(
                                        consumed = , ), ), 
                                step = slurm_client.models.v0_0_42_step_step.v0_0_42_step_step(
                                    name = '', ), 
                                task = slurm_client.models.v0_0_42_step_task.v0_0_42_step_task(
                                    distribution = '', ), 
                                tres = slurm_client.models.v0_0_42_step_tres.v0_0_42_step_tres(
                                    requested = slurm_client.models.v0_0_42_step_tres_requested.v0_0_42_step_tres_requested(
                                        average = [
                                            slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                                                type = '', 
                                                name = '', 
                                                count = 56, )
                                            ], ), 
                                    allocated = [
                                        slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                                            type = '', 
                                            name = '', 
                                            count = 56, )
                                        ], ), )
                            ], 
                        submit_line = '', 
                        tres = slurm_client.models.v0_0_42_job_tres.v0_0_42_job_tres(), 
                        used_gres = '', 
                        user = '', 
                        wckey = slurm_client.models.v0/0/42_wckey_tag_struct.v0.0.42_wckey_tag_struct(
                            wckey = '', 
                            flags = [
                                'ASSIGNED_DEFAULT'
                                ], ), 
                        working_directory = '', )
                    ],
        )
        """

    def testV0042OpenapiSlurmdbdJobsResp(self):
        """Test V0042OpenapiSlurmdbdJobsResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()