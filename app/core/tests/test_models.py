"""Test for models."""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test for models."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for a new user is normalized."""
        sample_email = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected_email in sample_email:
            user = get_user_model().objects.create_user(email=email, password='testpass123')
            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raises_exception(self):
        """Test creating a new user without an email raises an exception."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='', password='testpass123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('test@example.com', 'testpass123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
