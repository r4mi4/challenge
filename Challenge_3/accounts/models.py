from django.db import models
from rest_framework_api_key.models import AbstractAPIKey


class OrganizationAPIKey(AbstractAPIKey):
    active = models.BooleanField(default=True, null=True, blank=True)
    counter = models.PositiveIntegerField(null=True, blank=True)


class RestrictIp(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.name
