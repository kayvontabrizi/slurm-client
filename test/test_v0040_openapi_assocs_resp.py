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

from slurm_client.models.v0040_openapi_assocs_resp import V0040OpenapiAssocsResp

class TestV0040OpenapiAssocsResp(unittest.TestCase):
    """V0040OpenapiAssocsResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiAssocsResp:
        """Test V0040OpenapiAssocsResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiAssocsResp`
        """
        model = V0040OpenapiAssocsResp()
        if include_optional:
            return V0040OpenapiAssocsResp(
                associations = [
                    slurm_client.models.v0/0/40_assoc.v0.0.40_assoc(
                        accounting = [
                            slurm_client.models.v0/0/40_accounting.v0.0.40_accounting(
                                allocated = slurm_client.models.v0_0_40_accounting_allocated.v0_0_40_accounting_allocated(
                                    seconds = 56, ), 
                                id = 56, 
                                start = 56, 
                                tres = slurm_client.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '', 
                                    name = '', 
                                    id = 56, 
                                    count = 56, ), )
                            ], 
                        account = '', 
                        cluster = '', 
                        comment = '', 
                        default = slurm_client.models.v0_0_42_assoc_default.v0_0_42_assoc_default(
                            qos = '', ), 
                        flags = [
                            'DELETED'
                            ], 
                        max = slurm_client.models.v0_0_40_assoc_max.v0_0_40_assoc_max(
                            jobs = slurm_client.models.v0_0_40_assoc_max_jobs.v0_0_40_assoc_max_jobs(
                                per = slurm_client.models.v0_0_40_assoc_max_jobs_per.v0_0_40_assoc_max_jobs_per(
                                    count = slurm_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    accruing = slurm_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    submitted = , 
                                    wall_clock = , ), 
                                active = , 
                                accruing = , 
                                total = , ), 
                            tres = slurm_client.models.v0_0_40_assoc_max_tres.v0_0_40_assoc_max_tres(
                                group = slurm_client.models.v0_0_40_assoc_max_tres_group.v0_0_40_assoc_max_tres_group(
                                    minutes = [
                                        slurm_client.models.v0/0/40_tres.v0.0.40_tres(
                                            type = '', 
                                            name = '', 
                                            id = 56, )
                                        ], ), 
                                minutes = slurm_client.models.v0_0_40_assoc_max_tres_minutes.v0_0_40_assoc_max_tres_minutes(), ), 
                            per = slurm_client.models.v0_0_40_assoc_max_per.v0_0_40_assoc_max_per(
                                account = slurm_client.models.v0_0_40_assoc_max_per_account.v0_0_40_assoc_max_per_account(), ), ), 
                        id = slurm_client.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                            cluster = '', 
                            partition = '', 
                            user = '', ), 
                        is_default = True, 
                        lineage = '', 
                        min = slurm_client.models.v0_0_40_assoc_min.v0_0_40_assoc_min(
                            priority_threshold = , ), 
                        parent_account = '', 
                        partition = '', 
                        priority = , 
                        qos = [
                            ''
                            ], 
                        shares_raw = 56, 
                        user = '', )
                    ],
                meta = slurm_client.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
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
                    slurm_client.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    slurm_client.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0040OpenapiAssocsResp(
                associations = [
                    slurm_client.models.v0/0/40_assoc.v0.0.40_assoc(
                        accounting = [
                            slurm_client.models.v0/0/40_accounting.v0.0.40_accounting(
                                allocated = slurm_client.models.v0_0_40_accounting_allocated.v0_0_40_accounting_allocated(
                                    seconds = 56, ), 
                                id = 56, 
                                start = 56, 
                                tres = slurm_client.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '', 
                                    name = '', 
                                    id = 56, 
                                    count = 56, ), )
                            ], 
                        account = '', 
                        cluster = '', 
                        comment = '', 
                        default = slurm_client.models.v0_0_42_assoc_default.v0_0_42_assoc_default(
                            qos = '', ), 
                        flags = [
                            'DELETED'
                            ], 
                        max = slurm_client.models.v0_0_40_assoc_max.v0_0_40_assoc_max(
                            jobs = slurm_client.models.v0_0_40_assoc_max_jobs.v0_0_40_assoc_max_jobs(
                                per = slurm_client.models.v0_0_40_assoc_max_jobs_per.v0_0_40_assoc_max_jobs_per(
                                    count = slurm_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    accruing = slurm_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    submitted = , 
                                    wall_clock = , ), 
                                active = , 
                                accruing = , 
                                total = , ), 
                            tres = slurm_client.models.v0_0_40_assoc_max_tres.v0_0_40_assoc_max_tres(
                                group = slurm_client.models.v0_0_40_assoc_max_tres_group.v0_0_40_assoc_max_tres_group(
                                    minutes = [
                                        slurm_client.models.v0/0/40_tres.v0.0.40_tres(
                                            type = '', 
                                            name = '', 
                                            id = 56, )
                                        ], ), 
                                minutes = slurm_client.models.v0_0_40_assoc_max_tres_minutes.v0_0_40_assoc_max_tres_minutes(), ), 
                            per = slurm_client.models.v0_0_40_assoc_max_per.v0_0_40_assoc_max_per(
                                account = slurm_client.models.v0_0_40_assoc_max_per_account.v0_0_40_assoc_max_per_account(), ), ), 
                        id = slurm_client.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                            cluster = '', 
                            partition = '', 
                            user = '', ), 
                        is_default = True, 
                        lineage = '', 
                        min = slurm_client.models.v0_0_40_assoc_min.v0_0_40_assoc_min(
                            priority_threshold = , ), 
                        parent_account = '', 
                        partition = '', 
                        priority = , 
                        qos = [
                            ''
                            ], 
                        shares_raw = 56, 
                        user = '', )
                    ],
        )
        """

    def testV0040OpenapiAssocsResp(self):
        """Test V0040OpenapiAssocsResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
