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

from slurm_client.models.v0041_openapi_slurmdbd_config_resp_associations_inner import V0041OpenapiSlurmdbdConfigRespAssociationsInner

class TestV0041OpenapiSlurmdbdConfigRespAssociationsInner(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespAssociationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespAssociationsInner:
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespAssociationsInner`
        """
        model = V0041OpenapiSlurmdbdConfigRespAssociationsInner()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInner(
                accounting = [
                    slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner(
                        allocated = slurm_client.models.v0_0_40_accounting_allocated.v0_0_40_accounting_allocated(
                            seconds = 56, ), 
                        id = 56, 
                        start = 56, 
                        tres = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_tres.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_TRES(
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
                max = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max(
                    jobs = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs(
                        per = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per(
                            count = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            accruing = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            submitted = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per_submitted.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per_submitted(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            wall_clock = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        active = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_active.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_active(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        accruing = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_accruing.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_accruing(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        total = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_total.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_total(
                            set = True, 
                            infinite = True, 
                            number = 56, ), ), 
                    tres = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres(
                        group = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_group.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_group(
                            minutes = [
                                slurm_client.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                    type = '', 
                                    name = '', 
                                    id = 56, )
                                ], ), 
                        minutes = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes(), ), 
                    per = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_per.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_per(
                        account = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_per_account.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_per_account(), ), ),
                id = 56,
                is_default = True,
                lineage = '',
                min = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_min.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_min(
                    priority_threshold = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_priority_threshold.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_priority_threshold(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                parent_account = '',
                partition = '',
                priority = slurm_client.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_priority.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_priority(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                qos = [
                    ''
                    ],
                shares_raw = 56,
                user = ''
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInner(
                user = '',
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespAssociationsInner(self):
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
