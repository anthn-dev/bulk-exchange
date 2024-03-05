"""Serializer for users.

This module defines the UserSerializer class, a Django Rest Framework serializer
for the User model. It includes custom handling for password management.

Attributes:
    UserSerializer (class): Subclass of rest_framework.serializers.ModelSerializer.
"""

from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """User Serializer.

    Extends rest_framework.serializers.ModelSerializer to serialize and deserialize User objects.
    Includes custom handling for password management.

    Attributes:
        password (CharField): Write-only field for handling passwords during serialization.

    Meta:
        model (class): The User model.
        fields (tuple): Fields to be included in the serialized representation.

    Methods:
        create(validated_data): Creates a new user using the provided validated data.

        update(instance, validated_data): Updates an existing user instance with validated data,
        handling password updates and session authentication hash.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        """Meta object for users."""

        model = User
        fields = ("first_name", "last_name", "email", "password", "phone")

    def create(self, validated_data):
        """Create a new user.

        Args:
            validated_data (dict): Validated data containing user information.

        Returns:
            User: The newly created user object.
        """
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone=validated_data["phone"],
        )
        return user

    def update(self, instance, validated_data):
        """Update an existing user instance.

        Args:
            instance (User): The existing user instance.
            validated_data (dict): Validated data containing updated user information.

        Returns:
            User: The updated user object.
        """
        password = validated_data.get("password")

        if password:
            instance.set_password(password)
            update_session_auth_hash(self.context.get("request"), instance)
            validated_data.pop("password")

        return super().update(instance, validated_data)
