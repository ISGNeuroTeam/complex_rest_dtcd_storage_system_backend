import json
from rest.test import TestCase, APIClient

from dtcd_storage_system_backend.system.state import State


class TestStateView(TestCase):

    def setUp(self):
        """
        define instructions that will be executed before each test method
        """
        self.application_name = "testApp"
        self.scope_name = "testScope"
        self.workspace_id = "workspaceID=1"
        self.state_body = {"some": "state"}
        pass

    def test_save(self):
        client = APIClient()
        response = client.post(
            '/dtcd_storage_system_backend/v1/state/'.lower(),
            json.dumps({"workspaceID": self.workspace_id,
                        "applicationName": self.application_name, "state": self.state_body}),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        state_id = response.data["stateID"]
        self.assertTrue(state_id)

    def test_load(self):

        state = State(self.application_name)
        state_id = state.save(self.workspace_id, self.state_body)

        client = APIClient()
        response = client.get('/dtcd_storage_system_backend/v1/state/'.lower(),
                              data={"stateID": state_id, "applicationName": self.application_name})
        self.assertEqual(response.status_code, 200)
        message = response.data['state']
        self.assertEqual(message, self.state_body)

    def tearDown(self):
        """
        define instructions that will be executed after each test method
        """
        pass
