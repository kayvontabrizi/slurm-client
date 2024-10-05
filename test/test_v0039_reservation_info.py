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

from openapi_client.models.v0039_reservation_info import V0039ReservationInfo

class TestV0039ReservationInfo(unittest.TestCase):
    """V0039ReservationInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039ReservationInfo:
        """Test V0039ReservationInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039ReservationInfo`
        """
        model = V0039ReservationInfo()
        if include_optional:
            return V0039ReservationInfo(
                accounts = '',
                burst_buffer = '',
                core_count = 56,
                core_specializations = [
                    openapi_client.models.v0/0/39_reservation_core_spec.v0.0.39_reservation_core_spec(
                        node = '', 
                        core = '', )
                    ],
                end_time = 56,
                features = '',
                flags = [
                    'MAINT'
                    ],
                groups = '',
                licenses = '',
                max_start_delay = 56,
                name = '',
                node_count = 56,
                node_list = '',
                partition = '',
                purge_completed = openapi_client.models.v0_0_39_reservation_info_purge_completed.v0_0_39_reservation_info_purge_completed(
                    time = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                start_time = 56,
                watts = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                tres = '',
                users = ''
            )
        else:
            return V0039ReservationInfo(
        )
        """

    def testV0039ReservationInfo(self):
        """Test V0039ReservationInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
