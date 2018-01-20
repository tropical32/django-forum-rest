import datetime
from rest_framework import permissions


class IsNotBanned(permissions.BasePermission):
    def has_no_ban_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.banned_until.replace(
                tzinfo=None
        ) > datetime.datetime.now():
            return False
