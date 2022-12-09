from django.db import IntegrityError

from .models import StorageModel


class Storage:

    def __init__(self, application_name, extra=None, model=None):
        self.model = StorageModel if model is None else model
        self.extra = extra
        self.application_name = application_name

    def append_to_record(self, record):
        record = {"application_name": self.application_name, **record}
        if self.extra is not None:
            record = {**self.extra, **record}
        return record

    def add_record(self, record):
        record = self.append_to_record(record)
        _record = self.model(**record)
        _record.save()

    def put_record(self, record):
        record = self.append_to_record(record)
        _record = self.model(**record)
        try:
            _record.save()
        except IntegrityError:
            _record = self.model.objects.get(key=record["key"])
            _record.value = record["value"]
            _record.save()

    def get_record(self, record):
        record = self.append_to_record(record)
        record = self.model.objects.get(**record)
        return record

    def has_record(self, record):
        record = self.append_to_record(record)
        try:
            self.get_record(record)
            return True
        except self.model.DoesNotExist:
            return False

    def remove_record(self, record):
        record = self.append_to_record(record)
        record = self.get_record(record)
        response = record.delete()
        return response

    def clear_storage(self):
        response = self.model.objects.all().delete()
        return response

    def get_records_by_filter(self, filter_query):
        records = self.model.objects.filter(**filter_query)
        return records
