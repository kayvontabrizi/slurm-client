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

from slurm_client.models.v0040_cron_entry import V0040CronEntry

class TestV0040CronEntry(unittest.TestCase):
    """V0040CronEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040CronEntry:
        """Test V0040CronEntry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040CronEntry`
        """
        model = V0040CronEntry()
        if include_optional:
            return V0040CronEntry(
                flags = [
                    'WILD_MINUTE'
                    ],
                minute = '',
                hour = '',
                day_of_month = '',
                month = '',
                day_of_week = '',
                specification = '',
                command = '',
                line = slurm_client.models.v0_0_41_job_desc_msg_crontab_line.v0_0_41_job_desc_msg_crontab_line(
                    start = 56, 
                    end = 56, )
            )
        else:
            return V0040CronEntry(
        )
        """

    def testV0040CronEntry(self):
        """Test V0040CronEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
