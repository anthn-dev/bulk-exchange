"""Model for users.

This module defines the User model for the application, extending Django's AbstractUser.
It includes custom fields for email and phone, as well as a custom manager for user-related operations.

Attributes:
    User (class): Subclass of Django's AbstractUser, representing the User model.
"""

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from .manager import UserManager


class User(AbstractUser):
    """User Model.

    Extends Django's AbstractUser to include custom fields for email and phone.
    Uses a custom manager, UserManager, for user-related operations.

    Attributes:
        email (EmailField): A unique email address associated with the user.
        phone (CharField): A unique phone number associated with the user.

    Class Attributes:
        USERNAME_FIELD (str): Specifies the field used for authentication (email in this case).
        REQUIRED_FIELDS (list): List of additional fields required for creating a user.

    Methods:
        __str__(): Returns a string representation of the user, using the email address.

        clean(): Performs additional validation during model cleaning, checking for unique email and phone.
    """

    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        """Return a string representation of the user."""
        return self.email

    def clean(self):
        """Perform additional validation during model cleaning.

        Checks for unique email and phone to avoid duplication.

        Raises:
            ValidationError: If the email or phone is already in use.
        """
        if User.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError({"email": "This email address is already in use."})

        if User.objects.filter(phone=self.phone).exclude(pk=self.pk).exists():
            raise ValidationError({"phone": "This phone number is already in use."})
