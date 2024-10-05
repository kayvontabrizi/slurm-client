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

from slurm_client.models.v0041_openapi_kill_jobs_resp_status_inner_federation import V0041OpenapiKillJobsRespStatusInnerFederation

class TestV0041OpenapiKillJobsRespStatusInnerFederation(unittest.TestCase):
    """V0041OpenapiKillJobsRespStatusInnerFederation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiKillJobsRespStatusInnerFederation:
        """Test V0041OpenapiKillJobsRespStatusInnerFederation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiKillJobsRespStatusInnerFederation`
        """
        model = V0041OpenapiKillJobsRespStatusInnerFederation()
        if include_optional:
            return V0041OpenapiKillJobsRespStatusInnerFederation(
                sibling = ''
            )
        else:
            return V0041OpenapiKillJobsRespStatusInnerFederation(
        )
        """

    def testV0041OpenapiKillJobsRespStatusInnerFederation(self):
        """Test V0041OpenapiKillJobsRespStatusInnerFederation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
