from rest_framework import exceptions
from rest_framework_api_key.permissions import BaseHasAPIKey
from rest_framework.permissions import BasePermission
from .models import OrganizationAPIKey, RestrictIp
from django.conf import settings


class HasOrganizationAPIKey(BaseHasAPIKey):
    model = OrganizationAPIKey


class RateLimit(BasePermission):

    def has_permission(self, request, view):
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        api_key = OrganizationAPIKey.objects.get_from_key(key)
        if api_key.counter < settings.RATE_LIMIT_TO_API_KEY:
            api_key.counter += 1
            api_key.save()
            return True
        raise exceptions.PermissionDenied({'msg': 'limit reach'})


class ValidIp(BasePermission):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def has_permission(self, request, view):
        ip = self.get_client_ip(request)
        try:
            RestrictIp.objects.get(ip=ip)
            raise exceptions.PermissionDenied({'msg': 'sorry! your ip blocked'})
        except RestrictIp.DoesNotExist:
            return True
