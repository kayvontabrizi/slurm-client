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

from slurm_client.models.v0042_qos_limits_max_tres_minutes import V0042QosLimitsMaxTresMinutes

class TestV0042QosLimitsMaxTresMinutes(unittest.TestCase):
    """V0042QosLimitsMaxTresMinutes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042QosLimitsMaxTresMinutes:
        """Test V0042QosLimitsMaxTresMinutes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042QosLimitsMaxTresMinutes`
        """
        model = V0042QosLimitsMaxTresMinutes()
        if include_optional:
            return V0042QosLimitsMaxTresMinutes(
                total = [
                    slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                per = slurm_client.models.v0_0_42_qos_limits_max_tres_minutes_per.v0_0_42_qos_limits_max_tres_minutes_per(
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
                    account = , 
                    user = , )
            )
        else:
            return V0042QosLimitsMaxTresMinutes(
        )
        """

    def testV0042QosLimitsMaxTresMinutes(self):
        """Test V0042QosLimitsMaxTresMinutes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
