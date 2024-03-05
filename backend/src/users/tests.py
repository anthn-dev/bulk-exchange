"""Test cases for users app"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework import status

from .factory import TokenFactory, UserFactory, build_dict

fake = Faker()
User = get_user_model()


class UserRegistrationViewTest(TestCase):
    """Test for user registration"""

    def test_user_registration(self):
        """Test user registration"""

        url = reverse("register")
        data = UserFactory.build()
        data = build_dict(data)
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email=data.get("email")).exists())

    def test_missing_email_user_registration(self):
        """Test with missing email"""

        url = reverse("register")
        data = UserFactory.build(email="")
        data = build_dict(data)
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_error = {"email": ["This field may not be blank."]}
        self.assertDictEqual(response.data, expected_error)

    def test_invalid_email_user_registration(self):
        """Test with invalid email"""

        url = reverse("register")
        data = UserFactory.build(email="invalid-email")
        data = build_dict(data)
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_error = {"email": ["Enter a valid email address."]}
        self.assertDictEqual(response.data, expected_error)

    def test_duplicate_email_user_registration(self):
        """Test with duplicate email user registration"""

        existing_user = UserFactory.create()
        existing_user.save()

        url = reverse("register")
        data = UserFactory.build(email=existing_user.email)
        data = build_dict(data)
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_error = {"email": ["user with this email already exists."]}
        self.assertDictEqual(response.data, expected_error)

    def test_duplicate_phone_user_registration(self):
        """Test with duplicate phone user registration"""

        existing_user = UserFactory.create()
        existing_user.save()

        url = reverse("register")
        data = UserFactory.build(phone=existing_user.phone)
        data = build_dict(data)
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_error = {"phone": ["user with this phone already exists."]}
        self.assertDictEqual(response.data, expected_error)


class UserLoginViewTest(TestCase):
    """Test login"""

    def setUp(self):
        self.user = UserFactory.create()
        self.user.save()

    def test_user_login(self):
        """Test for login user"""

        url = reverse("login")
        data = {"email": self.user.email, "password": "my_super_secret"}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_invalid_credentials(self):
        """Test with invalid credentials"""

        url = reverse("login")
        data = {"email": fake.email(), "password": fake.password()}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("error", response.data)


class UserDetailsViewTest(TestCase):
    """Test the user details"""

    def setUp(self):
        self.user = UserFactory.create()
        self.user.save()
        self.token = TokenFactory(user=self.user)
        self.token.save()

    def test_user_details(self):
        """Test user details"""

        url = reverse("details")
        self.client.defaults["HTTP_AUTHORIZATION"] = f"Token {self.token.key}"
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)


class EditUserViewTest(TestCase):
    """Test edit user details"""

    def setUp(self):
        self.user = UserFactory.create()
        self.user.save()
        self.token = TokenFactory(user=self.user)
        self.token.save()

    def test_edit_user_profile(self):
        """Test edit user"""

        url = reverse("edit-profile")
        data = {"first_name": "John", "last_name": "Doe"}
        self.client.defaults["HTTP_AUTHORIZATION"] = f"Token {self.token.key}"
        response = self.client.patch(
            url, data, format="json", content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "John")
        self.assertEqual(response.data["last_name"], "Doe")
