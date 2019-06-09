from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful"""
        email = "email@server.com"
        password = "somepassword"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = "test@SERVER.com"
        user = get_user_model().objects.create_user(email, password="abc123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None, password="somepass"
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "someemail@somedomain.com",
            "somepassword"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
