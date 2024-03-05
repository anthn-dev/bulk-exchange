"""Config for users application"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
