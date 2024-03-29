from django.utils import timezone
from django.db import models


class StorageModel(models.Model):

    application_name = models.TextField()
    key = models.TextField(unique=True)
    value = models.JSONField(blank=True)

    class Meta:
        abstract = True


class ScopeModel(StorageModel):

    scope_name = models.TextField()


class StateModel(StorageModel):
    workspaceID = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
