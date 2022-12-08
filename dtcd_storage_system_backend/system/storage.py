from django.db import IntegrityError

from .models import StorageModel


class Storage:

    def __init__(self, model=None):
        self.model = StorageModel if model is None else model

    def add_record(self, record):
        _record = self.model(**record)
        _record.save()

    def put_record(self, record):
        _record = self.model(**record)
        try:
            _record.save()
        except IntegrityError:
            _record = self.model.objects.get(key=record["key"])
            _record.value = record["value"]
            _record.save()

    def get_record(self, key_record):
        record = self.model.objects.get(**key_record)
        return record

    def has_record(self, key_record):
        try:
            self.get_record(key_record)
            return True
        except self.model.DoesNotExist:
            return False

    def remove_record(self, key_record):
        record = self.get_record(key_record)
        response = record.delete()
        return response

    def clear_storage(self):
        response = self.model.objects.all().delete()
        return response
