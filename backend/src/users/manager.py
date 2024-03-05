"""Object Manager for users.

This module defines the UserManager class, a custom manager for the User model.
It extends Django's BaseUserManager and provides methods for creating regular users and superusers.

Attributes:
    UserManager (class): Subclass of Django's BaseUserManager, representing the object manager for the User model.
"""

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Object Manager for users.

    Extends Django's BaseUserManager to provide custom methods for user creation.

    Methods:
        create_user(email, password=None, **extra_fields): Creates a new user.

        create_superuser(email, password=None, **extra_fields): Creates a new superuser.

    Example:
        manager = UserManager()
        user = manager.create_user(email='user@example.com', password='securepassword')
        superuser = manager.create_superuser(email='admin@example.com', password='adminpassword')
    """

    def create_user(self, email, password=None, **extra_fields):
        """Create a new user.

        Args:
            email (str): Email address of the user.
            password (str): Password for the user.
            **extra_fields: Additional fields for the user model.

        Returns:
            User: The newly created user object.

        Raises:
            ValueError: If the email field is not provided.
        """
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create a new superuser.

        Args:
            email (str): Email address of the superuser.
            password (str): Password for the superuser.
            **extra_fields: Additional fields for the superuser model.

        Returns:
            User: The newly created superuser object.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
