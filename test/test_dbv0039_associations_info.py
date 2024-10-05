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

from openapi_client.models.dbv0039_associations_info import Dbv0039AssociationsInfo

class TestDbv0039AssociationsInfo(unittest.TestCase):
    """Dbv0039AssociationsInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039AssociationsInfo:
        """Test Dbv0039AssociationsInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039AssociationsInfo`
        """
        model = Dbv0039AssociationsInfo()
        if include_optional:
            return Dbv0039AssociationsInfo(
                meta = openapi_client.models.dbv0/0/39_meta.dbv0.0.39_meta(
                    plugin = openapi_client.models.v0_0_39_meta_plugin.v0_0_39_meta_plugin(
                        type = '', 
                        name = '', ), 
                    slurm = openapi_client.models.v0_0_39_meta_slurm.v0_0_39_meta_Slurm(
                        version = openapi_client.models.v0_0_39_meta_slurm_version.v0_0_39_meta_Slurm_version(
                            major = 56, 
                            micro = 56, 
                            minor = 56, ), 
                        release = '', ), ),
                errors = [
                    openapi_client.models.dbv0/0/39_error.dbv0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    openapi_client.models.dbv0/0/39_warning.dbv0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                associations = [
                    openapi_client.models.v0/0/39_assoc.v0.0.39_assoc(
                        account = '', 
                        cluster = '', 
                        default = openapi_client.models.v0_0_39_assoc_default.v0_0_39_assoc_default(
                            qos = '', ), 
                        flags = [
                            'DELETED'
                            ], 
                        max = openapi_client.models.v0_0_39_assoc_max.v0_0_39_assoc_max(
                            jobs = openapi_client.models.v0_0_39_assoc_max_jobs.v0_0_39_assoc_max_jobs(
                                per = openapi_client.models.v0_0_39_assoc_max_jobs_per.v0_0_39_assoc_max_jobs_per(
                                    count = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    accruing = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    submitted = , 
                                    wall_clock = , ), 
                                active = , 
                                accruing = , 
                                total = , ), 
                            tres = openapi_client.models.v0_0_39_assoc_max_tres.v0_0_39_assoc_max_tres(
                                minutes = openapi_client.models.v0_0_39_assoc_max_tres_minutes.v0_0_39_assoc_max_tres_minutes(), 
                                group = openapi_client.models.v0_0_39_assoc_max_tres_group.v0_0_39_assoc_max_tres_group(), ), 
                            per = openapi_client.models.v0_0_39_assoc_max_per.v0_0_39_assoc_max_per(
                                account = openapi_client.models.v0_0_39_assoc_max_per_account.v0_0_39_assoc_max_per_account(), ), ), 
                        is_default = True, 
                        min = openapi_client.models.v0_0_39_assoc_min.v0_0_39_assoc_min(
                            priority_threshold = , ), 
                        parent_account = '', 
                        partition = '', 
                        priority = , 
                        qos = [
                            ''
                            ], 
                        shares_raw = 56, 
                        usage = openapi_client.models.v0/0/39_assoc_usage.v0.0.39_assoc_usage(
                            accrue_job_count = 56, 
                            group_used_wallclock = 1.337, 
                            fairshare_factor = 1.337, 
                            fairshare_shares = 56, 
                            normalized_priority = 1.337, 
                            normalized_shares = 1.337, 
                            effective_normalized_usage = 1.337, 
                            normalized_usage = 1.337, 
                            raw_usage = 1.337, 
                            active_jobs = 56, 
                            job_count = 56, 
                            fairshare_level = 1.337, ), 
                        user = '', )
                    ]
            )
        else:
            return Dbv0039AssociationsInfo(
        )
        """

    def testDbv0039AssociationsInfo(self):
        """Test Dbv0039AssociationsInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
