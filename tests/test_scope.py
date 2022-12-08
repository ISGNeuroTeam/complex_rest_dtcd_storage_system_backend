from rest.test import TestCase

from dtcd_storage_system_backend.system.scope import Scope


class TestScope(TestCase):

    def setUp(self) -> None:
        self.scope = Scope()

    def test_add_record(self):
        record = {"key": "k1", "value": "v1"}
        first = 1
        self.scope.add_record(record)
        second = self.scope.model.objects.count()
        self.assertEqual(first, second)

    def test_put_record(self):
        record = {"key": "k1", "value": "v1"}
        first = 1
        self.scope.put_record(record)
        second = self.scope.model.objects.count()
        self.assertEqual(first, second)

    def test_get_record(self):
        self.scope.add_record({"key": "k1", "value": "v1"})
        record = {"key": "k1"}
        first = "v1"
        second = self.scope.get_record(record).value
        self.assertEqual(first, second)

    def test_has_record(self):
        self.scope.add_record({"key": "k1", "value": "v1"})
        record = {"key": "k1"}
        first = True
        second = self.scope.has_record(record)
        self.assertEqual(first, second)
        record = {"key": "k2"}
        first = False
        second = self.scope.has_record(record)
        self.assertEqual(first, second)

    def test_remove_record(self):
        record = {"key": "k1", "value": "v1"}
        self.scope.add_record(record)
        self.assertEqual(1, self.scope.model.objects.count())
        self.scope.remove_record(record)
        self.assertEqual(0, self.scope.model.objects.count())

    def test_clear_storage(self):
        for i in range(3):
            record = {"key": f"k{i}", "value": f"v{i}"}
            self.scope.add_record(record)
        self.assertEqual(3, self.scope.model.objects.count())
        self.scope.clear_storage()
        self.assertEqual(0, self.scope.model.objects.count())
