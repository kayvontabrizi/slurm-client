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

from slurm_client.models.v0042_assoc import V0042Assoc

class TestV0042Assoc(unittest.TestCase):
    """V0042Assoc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042Assoc:
        """Test V0042Assoc
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042Assoc`
        """
        model = V0042Assoc()
        if include_optional:
            return V0042Assoc(
                accounting = [
                    slurm_client.models.v0/0/42_accounting.v0.0.42_accounting(
                        allocated = slurm_client.models.v0_0_42_accounting_allocated.v0_0_42_accounting_allocated(
                            seconds = 56, ), 
                        id = 56, 
                        id_alt = 56, 
                        start = 56, 
                        tres = slurm_client.models.v0/0/42_tres.v0.0.42_tres(
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
                max = slurm_client.models.v0_0_42_assoc_max.v0_0_42_assoc_max(
                    jobs = slurm_client.models.v0_0_42_assoc_max_jobs.v0_0_42_assoc_max_jobs(
                        per = slurm_client.models.v0_0_42_assoc_max_jobs_per.v0_0_42_assoc_max_jobs_per(
                            count = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            accruing = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            submitted = , 
                            wall_clock = , ), 
                        active = , 
                        accruing = , 
                        total = , ), 
                    tres = slurm_client.models.v0_0_42_assoc_max_tres.v0_0_42_assoc_max_tres(
                        group = slurm_client.models.v0_0_42_assoc_max_tres_group.v0_0_42_assoc_max_tres_group(
                            minutes = [
                                slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                                    type = '', 
                                    name = '', 
                                    id = 56, )
                                ], ), 
                        minutes = slurm_client.models.v0_0_42_assoc_max_tres_minutes.v0_0_42_assoc_max_tres_minutes(), ), 
                    per = slurm_client.models.v0_0_42_assoc_max_per.v0_0_42_assoc_max_per(
                        account = slurm_client.models.v0_0_42_assoc_max_per_account.v0_0_42_assoc_max_per_account(), ), ),
                id = 56,
                is_default = True,
                lineage = '',
                min = slurm_client.models.v0_0_42_assoc_min.v0_0_42_assoc_min(
                    priority_threshold = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                parent_account = '',
                partition = '',
                priority = slurm_client.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
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
            return V0042Assoc(
                user = '',
        )
        """

    def testV0042Assoc(self):
        """Test V0042Assoc"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()