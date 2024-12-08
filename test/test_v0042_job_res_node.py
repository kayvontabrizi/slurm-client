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

from slurm_client.models.v0042_job_res_node import V0042JobResNode

class TestV0042JobResNode(unittest.TestCase):
    """V0042JobResNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042JobResNode:
        """Test V0042JobResNode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0042JobResNode`
        """
        model = V0042JobResNode()
        if include_optional:
            return V0042JobResNode(
                index = 56,
                name = '',
                cpus = slurm_client.models.v0_0_42_job_res_node_cpus.v0_0_42_job_res_node_cpus(
                    count = 56, 
                    used = 56, ),
                memory = slurm_client.models.v0_0_42_job_res_node_memory.v0_0_42_job_res_node_memory(
                    used = 56, 
                    allocated = 56, ),
                sockets = [
                    slurm_client.models.v0/0/42_job_res_socket.v0.0.42_job_res_socket(
                        index = 56, 
                        cores = [
                            slurm_client.models.v0/0/42_job_res_core.v0.0.42_job_res_core(
                                index = 56, 
                                status = [
                                    'INVALID'
                                    ], )
                            ], )
                    ]
            )
        else:
            return V0042JobResNode(
                index = 56,
                name = '',
                sockets = [
                    slurm_client.models.v0/0/42_job_res_socket.v0.0.42_job_res_socket(
                        index = 56, 
                        cores = [
                            slurm_client.models.v0/0/42_job_res_core.v0.0.42_job_res_core(
                                index = 56, 
                                status = [
                                    'INVALID'
                                    ], )
                            ], )
                    ],
        )
        """

    def testV0042JobResNode(self):
        """Test V0042JobResNode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()