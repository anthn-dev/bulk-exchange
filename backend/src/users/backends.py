"""Authentication Backend for users.

This module defines the EmailBackend class, a custom authentication backend for the User model.
It extends Django's ModelBackend and provides methods for authenticating users based on email.

Attributes:
    EmailBackend (class): Subclass of Django's ModelBackend, representing the email
    authentication backend for the User model.
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class EmailBackend(ModelBackend):
    """Email authentication backend for users.

    Extends Django's ModelBackend to provide email-based authentication.

    Methods:
        authenticate(request, email=None, password=None, **kwargs): Authenticates user by email.

        get_user(user_id): Retrieves a user by ID.

    Example:
        backend = EmailBackend()
        user = backend.authenticate(request, email='user@example.com', password='securepassword')
        user_by_id = backend.get_user(user_id=1)
    """

    def authenticate(self, request, email=None, password=None, **kwargs):
        """Authenticate user by email.

        Args:
            request: The current request.
            email (str): Email address of the user.
            password (str): Password for the user.
            **kwargs: Additional keyword arguments.

        Returns:
            User: The authenticated user object or None if authentication fails.
        """
        user_model = get_user_model()
        try:
            user = user_model.objects.get(Q(email__iexact=email))
        except user_model.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        """Get user by ID.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            User: The user object or None if the user does not exist.
        """
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
