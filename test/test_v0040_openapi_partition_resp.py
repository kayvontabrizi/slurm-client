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

from openapi_client.models.v0040_openapi_partition_resp import V0040OpenapiPartitionResp

class TestV0040OpenapiPartitionResp(unittest.TestCase):
    """V0040OpenapiPartitionResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiPartitionResp:
        """Test V0040OpenapiPartitionResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiPartitionResp`
        """
        model = V0040OpenapiPartitionResp()
        if include_optional:
            return V0040OpenapiPartitionResp(
                partitions = [
                    openapi_client.models.v0/0/40_partition_info.v0.0.40_partition_info(
                        nodes = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_nodes.v0_0_41_openapi_partition_resp_partitions_inner_nodes(
                            allowed_allocation = '', 
                            configured = '', 
                            total = 56, ), 
                        accounts = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_accounts.v0_0_41_openapi_partition_resp_partitions_inner_accounts(
                            allowed = '', 
                            deny = '', ), 
                        groups = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_groups.v0_0_41_openapi_partition_resp_partitions_inner_groups(
                            allowed = '', ), 
                        qos = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_qos.v0_0_41_openapi_partition_resp_partitions_inner_qos(
                            allowed = '', 
                            deny = '', 
                            assigned = '', ), 
                        alternate = '', 
                        tres = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_tres.v0_0_41_openapi_partition_resp_partitions_inner_tres(
                            billing_weights = '', 
                            configured = '', ), 
                        cluster = '', 
                        cpus = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_cpus.v0_0_41_openapi_partition_resp_partitions_inner_cpus(
                            task_binding = 56, 
                            total = 56, ), 
                        defaults = openapi_client.models.v0_0_40_partition_info_defaults.v0_0_40_partition_info_defaults(
                            memory_per_cpu = 56, 
                            partition_memory_per_cpu = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            partition_memory_per_node = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            time = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            job = '', ), 
                        grace_time = 56, 
                        maximums = openapi_client.models.v0_0_40_partition_info_maximums.v0_0_40_partition_info_maximums(
                            cpus_per_node = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            cpus_per_socket = , 
                            memory_per_cpu = 56, 
                            shares = 56, 
                            oversubscribe = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums_oversubscribe.v0_0_41_openapi_partition_resp_partitions_inner_maximums_oversubscribe(
                                jobs = 56, 
                                flags = [
                                    'force'
                                    ], ), 
                            over_time_limit = openapi_client.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        minimums = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_minimums.v0_0_41_openapi_partition_resp_partitions_inner_minimums(), 
                        name = '', 
                        node_sets = '', 
                        priority = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_priority.v0_0_41_openapi_partition_resp_partitions_inner_priority(
                            job_factor = 56, 
                            tier = 56, ), 
                        timeouts = openapi_client.models.v0_0_40_partition_info_timeouts.v0_0_40_partition_info_timeouts(
                            resume = openapi_client.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            suspend = , ), 
                        partition = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_partition.v0_0_41_openapi_partition_resp_partitions_inner_partition(
                            state = [
                                'INACTIVE'
                                ], ), 
                        suspend_time = , )
                    ],
                last_update = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                meta = openapi_client.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
                    plugin = openapi_client.models.v0_0_41_openapi_shares_resp_meta_plugin.v0_0_41_openapi_shares_resp_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = openapi_client.models.v0_0_41_openapi_shares_resp_meta_client.v0_0_41_openapi_shares_resp_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = openapi_client.models.v0_0_41_openapi_shares_resp_meta_slurm.v0_0_41_openapi_shares_resp_meta_slurm(
                        version = openapi_client.models.v0_0_41_openapi_shares_resp_meta_slurm_version.v0_0_41_openapi_shares_resp_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', 
                        cluster = '', ), ),
                errors = [
                    openapi_client.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    openapi_client.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0040OpenapiPartitionResp(
                partitions = [
                    openapi_client.models.v0/0/40_partition_info.v0.0.40_partition_info(
                        nodes = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_nodes.v0_0_41_openapi_partition_resp_partitions_inner_nodes(
                            allowed_allocation = '', 
                            configured = '', 
                            total = 56, ), 
                        accounts = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_accounts.v0_0_41_openapi_partition_resp_partitions_inner_accounts(
                            allowed = '', 
                            deny = '', ), 
                        groups = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_groups.v0_0_41_openapi_partition_resp_partitions_inner_groups(
                            allowed = '', ), 
                        qos = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_qos.v0_0_41_openapi_partition_resp_partitions_inner_qos(
                            allowed = '', 
                            deny = '', 
                            assigned = '', ), 
                        alternate = '', 
                        tres = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_tres.v0_0_41_openapi_partition_resp_partitions_inner_tres(
                            billing_weights = '', 
                            configured = '', ), 
                        cluster = '', 
                        cpus = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_cpus.v0_0_41_openapi_partition_resp_partitions_inner_cpus(
                            task_binding = 56, 
                            total = 56, ), 
                        defaults = openapi_client.models.v0_0_40_partition_info_defaults.v0_0_40_partition_info_defaults(
                            memory_per_cpu = 56, 
                            partition_memory_per_cpu = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            partition_memory_per_node = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            time = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            job = '', ), 
                        grace_time = 56, 
                        maximums = openapi_client.models.v0_0_40_partition_info_maximums.v0_0_40_partition_info_maximums(
                            cpus_per_node = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            cpus_per_socket = , 
                            memory_per_cpu = 56, 
                            shares = 56, 
                            oversubscribe = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums_oversubscribe.v0_0_41_openapi_partition_resp_partitions_inner_maximums_oversubscribe(
                                jobs = 56, 
                                flags = [
                                    'force'
                                    ], ), 
                            over_time_limit = openapi_client.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        minimums = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_minimums.v0_0_41_openapi_partition_resp_partitions_inner_minimums(), 
                        name = '', 
                        node_sets = '', 
                        priority = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_priority.v0_0_41_openapi_partition_resp_partitions_inner_priority(
                            job_factor = 56, 
                            tier = 56, ), 
                        timeouts = openapi_client.models.v0_0_40_partition_info_timeouts.v0_0_40_partition_info_timeouts(
                            resume = openapi_client.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            suspend = , ), 
                        partition = openapi_client.models.v0_0_41_openapi_partition_resp_partitions_inner_partition.v0_0_41_openapi_partition_resp_partitions_inner_partition(
                            state = [
                                'INACTIVE'
                                ], ), 
                        suspend_time = , )
                    ],
                last_update = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
        )
        """

    def testV0040OpenapiPartitionResp(self):
        """Test V0040OpenapiPartitionResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()