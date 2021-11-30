from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin
from .models import OrganizationAPIKey, RestrictIp


@admin.register(OrganizationAPIKey)
class OrganizationAPIKeyModelAdmin(APIKeyModelAdmin):
    List_display = [*APIKeyModelAdmin.list_display, "organization__name"]
    search_fields = [*APIKeyModelAdmin.search_fields, "organization__name"]


@admin.register(RestrictIp)
class RestrictIpModelAdmin(admin.ModelAdmin):
    list_display = ('ip', 'name')
