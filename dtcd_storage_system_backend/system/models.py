from django.utils import timezone
from django.db import models


class StorageModel(models.Model):

    created_at = models.DateField(default=timezone.now, blank=True)
    updated_at = models.DateField(default=timezone.now, blank=True)
    deleted_at = models.DateField(null=True, blank=True)

    application_name = models.TextField()
    key = models.TextField(unique=True)
    value = models.JSONField()

    class Meta:
        abstract = True


class ScopeModel(StorageModel):

    scope_name = models.TextField()

    # class Meta:
    #     abstract = True
