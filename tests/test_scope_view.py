import json
from rest.test import TestCase, APIClient

from dtcd_storage_system_backend.system.scope import Scope


class TestScopeView(TestCase):
    def setUp(self):
        """
        define instructions that will be executed before each test method
        """
        self.application_name = "testApp"
        self.scope_name = "testScope"
        pass

    def test_add_record(self):
        client = APIClient()
        response = client.post(
            '/dtcd_storage_system_backend/v1/scope/'.lower(),
            json.dumps({"record": {"key": "k1", "value": "v1"},
                        "applicationName": self.application_name, "scopeName": self.scope_name}),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

    def test_get_record(self):

        scope = Scope(self.application_name, self.scope_name)
        scope.add_record({"key": "k1", "value": "v1"})

        client = APIClient()
        response = client.get('/dtcd_storage_system_backend/v1/scope/'.lower(),
                              data={"key": "k1",
                                    "applicationName": self.application_name, "scopeName": self.scope_name})
        self.assertEqual(response.status_code, 200)
        message = response.data['value']
        self.assertEqual(message, 'v1')

    def tearDown(self):
        """
        define instructions that will be executed after each test method
        """
        pass
