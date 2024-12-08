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

from slurm_client.models.v0042_qos_limits_max_tres import V0042QosLimitsMaxTres

class TestV0042QosLimitsMaxTres(unittest.TestCase):
    """V0042QosLimitsMaxTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042QosLimitsMaxTres:
        """Test V0042QosLimitsMaxTres
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042QosLimitsMaxTres`
        """
        model = V0042QosLimitsMaxTres()
        if include_optional:
            return V0042QosLimitsMaxTres(
                total = [
                    slurm_client.models.v0/0/42_tres.v0.0.42_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                minutes = slurm_client.models.v0_0_42_qos_limits_max_tres_minutes.v0_0_42_qos_limits_max_tres_minutes(
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
                        job = , 
                        account = , 
                        user = , ), ),
                per = slurm_client.models.v0_0_42_qos_limits_max_tres_per.v0_0_42_qos_limits_max_tres_per(
                    account = [
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
                    node = , 
                    user = , )
            )
        else:
            return V0042QosLimitsMaxTres(
        )
        """

    def testV0042QosLimitsMaxTres(self):
        """Test V0042QosLimitsMaxTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
