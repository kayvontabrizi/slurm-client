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

from slurm_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association import V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation

class TestV0041OpenapiSlurmdbdJobsRespJobsInnerAssociation(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation(
                account = '',
                cluster = '',
                partition = '',
                user = '',
                id = 56
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation(
                user = '',
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInnerAssociation(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
