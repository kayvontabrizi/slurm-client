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

from openapi_client.models.v0041_update_node_msg_resume_after import V0041UpdateNodeMsgResumeAfter

class TestV0041UpdateNodeMsgResumeAfter(unittest.TestCase):
    """V0041UpdateNodeMsgResumeAfter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041UpdateNodeMsgResumeAfter:
        """Test V0041UpdateNodeMsgResumeAfter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041UpdateNodeMsgResumeAfter`
        """
        model = V0041UpdateNodeMsgResumeAfter()
        if include_optional:
            return V0041UpdateNodeMsgResumeAfter(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041UpdateNodeMsgResumeAfter(
        )
        """

    def testV0041UpdateNodeMsgResumeAfter(self):
        """Test V0041UpdateNodeMsgResumeAfter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()