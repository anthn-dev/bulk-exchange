"""Custom Permissions.

This module defines custom permissions for use with Django Rest Framework.

Attributes:
    IsOwner (class): Subclass of rest_framework.permissions.BasePermission.
"""

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Check if a user is the owner of an object.

    This permission is designed to be used with Django Rest Framework to restrict
    access to resources based on ownership.

    Attributes:
        message (str): A default error message to be used when permission is denied.

    Methods:
        has_object_permission(request, view, obj): Check if the requesting user is the owner of the object.
    """

    def has_object_permission(self, request, view, obj):
        """Check if the requesting user is the owner of the object.

        Args:
            request: The incoming request.
            view: The DRF view handling the request.
            obj: The object being accessed.

        Returns:
            bool: True if the user is the owner, False otherwise.
        """
        return obj.user == request.user
