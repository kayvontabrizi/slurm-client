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

from slurm_client.models.v0042_qos_limits_max_tres_minutes_per import V0042QosLimitsMaxTresMinutesPer

class TestV0042QosLimitsMaxTresMinutesPer(unittest.TestCase):
    """V0042QosLimitsMaxTresMinutesPer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042QosLimitsMaxTresMinutesPer:
        """Test V0042QosLimitsMaxTresMinutesPer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042QosLimitsMaxTresMinutesPer`
        """
        model = V0042QosLimitsMaxTresMinutesPer()
        if include_optional:
            return V0042QosLimitsMaxTresMinutesPer(
                qos = [
                    slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                job = [
                    slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                account = [
                    slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                user = [
                    slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return V0042QosLimitsMaxTresMinutesPer(
        )
        """

    def testV0042QosLimitsMaxTresMinutesPer(self):
        """Test V0042QosLimitsMaxTresMinutesPer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
