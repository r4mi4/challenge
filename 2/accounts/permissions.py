from rest_framework.permissions import BasePermission

from .models import BlackToken


class IsTokenValid(BasePermission):
    def has_permission(self, request, view):
        is_allowed_user = True
        token = request.auth
        try:
            is_blackListed = BlackToken.objects.get(user=request.user.id, token=token)
            if is_blackListed:
                is_allowed_user = False
        except BlackToken.DoesNotExist:
            is_allowed_user = True
        return is_allowed_user


"""
    NOTE: if we want to check owner really
            then we can use the following class

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
"""
