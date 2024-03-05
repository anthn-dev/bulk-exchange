"""User Factory for testing.

This module defines a factory class, UserFactory, for creating User instances during testing.
It uses the Factory package and Faker library to generate realistic and randomized user data.

Attributes:
    UserFactory (class): Factory class for generating User instances.
"""

import factory
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from factory import Factory
from factory import Faker as FactoryFaker
from factory import SubFactory
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserFactory(Factory):
    """Factory class for generating User instances during testing.

    This factory generates User instances with randomized data using the Faker library.

    Attributes:
        email (str): A randomized email address.
        password (str): A fixed password for testing purposes.
        phone (str): A randomized phone number.
        first_name (str): A randomized first name.
        last_name (str): A randomized last name.
    """

    class Meta:
        """Meta object for users."""

        model = User

    email = FactoryFaker("email")
    password = factory.PostGenerationMethodCall("set_password", "my_super_secret")
    phone = FactoryFaker("phone_number", locale="en_US")
    first_name = FactoryFaker("first_name")
    last_name = FactoryFaker("last_name")


class TokenFactory(Factory):
    """Factory class for generating Token instances during testing for user.

    This factory generates User instances with randomized data using the Faker library.

    Attributes:
        user (User): A User instance.
        key (str): A randomized token key.
    """

    class Meta:
        """Meta object for tokens."""

        model = Token

    user = SubFactory(UserFactory)
    key = get_random_string(length=40)


def build_dict(cls, **kwargs):
    default_data = {
        "email": cls.email,
        "password": cls.password,
        "phone": cls.phone,
        "first_name": cls.first_name,
        "last_name": cls.last_name,
    }
    default_data.update(kwargs)
    return default_data
