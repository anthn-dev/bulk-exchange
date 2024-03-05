"""URL patterns for the user app.

This module defines URL patterns for user-related views in the application.
It includes paths for user registration, login, profile update, and user details.

Attributes:
    urlpatterns (list): List of URL patterns for the user app.
"""

from django.urls import path

from .views import (EditUserView, UserDetailsView, UserLoginView,
                    UserRegistrationView)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("update/", EditUserView.as_view(), name="edit-profile"),
    path("details/", UserDetailsView.as_view(), name="details"),
]
