"""Views for users.

This module defines views for user-related operations using Django Rest Framework.

Attributes:
    UserRegistrationView (class): Subclass of rest_framework.generics.CreateAPIView.
    UserLoginView (class): Subclass of rest_framework.views.APIView for user login.
    UserDetailsView (class): Subclass of rest_framework.generics.RetrieveAPIView for user details.
    EditUserView (class): Subclass of rest_framework.generics.UpdateAPIView for editing user information.
"""

from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwner
from .serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    """View for user registration.

    Extends rest_framework.generics.CreateAPIView to handle user registration.
    Allows any user to access this view.

    Attributes:
        serializer_class (class): The serializer class for user registration.
        permission_classes (tuple): Tuple of permissions, allowing any user to access this view.
    """

    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class UserLoginView(APIView):
    """View for user login.

    Extends rest_framework.views.APIView to handle user login.
    Authenticates the user and returns a token upon successful login.

    Methods:
        post(request): Handles the POST request for user login.

    Example:
        To authenticate a user, send a POST request with email and password.
        If successful, a token will be returned.
    """

    def post(self, request):
        """Login user.

        Args:
            request: The incoming request containing user credentials.

        Returns:
            Response: A response containing a token upon successful login,
                      or an error message for invalid credentials.
        """
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})

        return Response({"error": "Invalid credentials"}, status=401)


class UserDetailsView(generics.RetrieveAPIView):
    """View for user details.

    Extends rest_framework.generics.RetrieveAPIView to retrieve user details.
    Requires authentication to access this view.

    Attributes:
        serializer_class (class): The serializer class for user details.
        permission_classes (tuple): Tuple of permissions, requiring user authentication to access this view.

    Methods:
        get_object(): Retrieves the user object based on the current authenticated user.
    """

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Get user details.

        Returns:
            User: The user object of the currently authenticated user.
        """
        return self.request.user


class EditUserView(generics.UpdateAPIView):
    """View for editing user information.

    Extends rest_framework.generics.UpdateAPIView to edit user information.
    Requires authentication and checks if the requesting user is the owner.

    Attributes:
        permission_classes (tuple): Tuple of permissions, requiring user
            authentication and ownership to access this view.
        serializer_class (class): The serializer class for editing user information.

    Methods:
        get_object(): Retrieves the user object based on the current authenticated user.
    """

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner,
    )
    serializer_class = UserSerializer

    def get_object(self):
        """Get user object for editing.

        Returns:
            User: The user object of the currently authenticated user.
        """
        return self.request.user
