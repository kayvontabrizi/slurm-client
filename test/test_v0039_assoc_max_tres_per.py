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

from slurm_client.models.v0039_assoc_max_tres_per import V0039AssocMaxTresPer

class TestV0039AssocMaxTresPer(unittest.TestCase):
    """V0039AssocMaxTresPer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039AssocMaxTresPer:
        """Test V0039AssocMaxTresPer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039AssocMaxTresPer`
        """
        model = V0039AssocMaxTresPer()
        if include_optional:
            return V0039AssocMaxTresPer(
                job = [
                    slurm_client.models.v0/0/39_tres.v0.0.39_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                node = [
                    slurm_client.models.v0/0/39_tres.v0.0.39_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return V0039AssocMaxTresPer(
        )
        """

    def testV0039AssocMaxTresPer(self):
        """Test V0039AssocMaxTresPer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
