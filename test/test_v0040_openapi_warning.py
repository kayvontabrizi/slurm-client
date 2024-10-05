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

from openapi_client.models.v0040_openapi_warning import V0040OpenapiWarning

class TestV0040OpenapiWarning(unittest.TestCase):
    """V0040OpenapiWarning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiWarning:
        """Test V0040OpenapiWarning
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiWarning`
        """
        model = V0040OpenapiWarning()
        if include_optional:
            return V0040OpenapiWarning(
                description = '',
                source = ''
            )
        else:
            return V0040OpenapiWarning(
        )
        """

    def testV0040OpenapiWarning(self):
        """Test V0040OpenapiWarning"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
