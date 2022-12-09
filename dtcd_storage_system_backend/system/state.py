import uuid
from datetime import timedelta
from django.utils import timezone

from .models import StateModel
from .storage import Storage


class State(Storage):

    def __init__(self, application_name, ttl=3600):
        super().__init__(application_name=application_name, model=StateModel)
        self.ttl = ttl

    def save(self, workspace_id, state):
        record = {"key": uuid.uuid3(uuid.NAMESPACE_DNS, workspace_id), "workspaceID": workspace_id, "value": state}
        self.add_record(record)
        return record["key"]

    def load(self, uid):
        record = {"key": uid}
        record = self.get_record(record)
        return record.value

    def remove_old(self):
        records = self.model.objects.filter(created_at__lt=timezone.now() - timedelta(seconds=self.ttl))
        records.delete()
