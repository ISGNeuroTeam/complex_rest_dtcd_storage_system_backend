import time

from rest.test import TestCase
from dtcd_storage_system_backend.system.state import State


class TestScope(TestCase):

    def setUp(self) -> None:
        self.state = State("testApp", 2)

    def test_save(self):
        workspace_id = "workspaceID=1"
        state_body = {"some": "state"}
        uid = self.state.save(workspace_id, state_body)
        second = self.state.get_record({"key": uid}).value
        self.assertEqual(state_body, second)

    def test_load(self):
        workspace_id = "workspaceID=1"
        state_body = {"some": "state"}
        uid = "123"
        record = {"key": uid, "workspaceID": workspace_id, "value": state_body}
        self.state.add_record(record)
        second = self.state.load(uid)
        self.assertEqual(state_body, second)

    def test_remove_old(self):
        workspace_id = "workspaceID=1"
        state_body = {"some": "state"}
        self.state.save(workspace_id, state_body)
        self.state.remove_old()
        first = 1
        second = self.state.model.objects.count()
        self.assertEqual(first, second)
        time.sleep(2)
        self.state.remove_old()
        first = 0
        second = self.state.model.objects.count()
        self.assertEqual(first, second)
