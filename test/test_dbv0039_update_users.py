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

from openapi_client.models.dbv0039_update_users import Dbv0039UpdateUsers

class TestDbv0039UpdateUsers(unittest.TestCase):
    """Dbv0039UpdateUsers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039UpdateUsers:
        """Test Dbv0039UpdateUsers
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039UpdateUsers`
        """
        model = Dbv0039UpdateUsers()
        if include_optional:
            return Dbv0039UpdateUsers(
                users = [
                    openapi_client.models.v0/0/39_user.v0.0.39_user(
                        administrator_level = [
                            'Not Set'
                            ], 
                        associations = [
                            openapi_client.models.v0/0/39_assoc_short.v0.0.39_assoc_short(
                                account = '', 
                                cluster = '', 
                                partition = '', 
                                user = '', )
                            ], 
                        coordinators = [
                            openapi_client.models.v0/0/39_coord.v0.0.39_coord(
                                name = '', 
                                direct = True, )
                            ], 
                        default = openapi_client.models.v0_0_39_user_default.v0_0_39_user_default(
                            account = '', 
                            wckey = '', ), 
                        flags = [
                            'NONE'
                            ], 
                        name = '', 
                        old_name = '', 
                        wckeys = [
                            openapi_client.models.v0/0/39_wckey.v0.0.39_wckey(
                                accounting = [
                                    openapi_client.models.v0/0/39_accounting.v0.0.39_accounting(
                                        allocated = openapi_client.models.v0_0_39_accounting_allocated.v0_0_39_accounting_allocated(
                                            seconds = 56, ), 
                                        id = 56, 
                                        start = 56, 
                                        tres = openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                                            type = '', 
                                            name = '', 
                                            id = 56, 
                                            count = 56, ), )
                                    ], 
                                cluster = '', 
                                id = 56, 
                                name = '', 
                                user = '', )
                            ], )
                    ]
            )
        else:
            return Dbv0039UpdateUsers(
        )
        """

    def testDbv0039UpdateUsers(self):
        """Test Dbv0039UpdateUsers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()