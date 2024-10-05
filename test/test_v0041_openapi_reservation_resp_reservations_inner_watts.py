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

from openapi_client.models.v0041_openapi_reservation_resp_reservations_inner_watts import V0041OpenapiReservationRespReservationsInnerWatts

class TestV0041OpenapiReservationRespReservationsInnerWatts(unittest.TestCase):
    """V0041OpenapiReservationRespReservationsInnerWatts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiReservationRespReservationsInnerWatts:
        """Test V0041OpenapiReservationRespReservationsInnerWatts
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiReservationRespReservationsInnerWatts`
        """
        model = V0041OpenapiReservationRespReservationsInnerWatts()
        if include_optional:
            return V0041OpenapiReservationRespReservationsInnerWatts(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiReservationRespReservationsInnerWatts(
        )
        """

    def testV0041OpenapiReservationRespReservationsInnerWatts(self):
        """Test V0041OpenapiReservationRespReservationsInnerWatts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()