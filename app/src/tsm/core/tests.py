from django.test import TestCase

from .models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="teacher1", password="teacher1")
        User.objects.create(username="teacher2", password="teacher2", first_name="first", last_name="last")

    def test_user_has_name_as_username(self):
        """Animals that can speak are correctly identified"""
        user = User.objects.get(username="teacher1")
        self.assertEqual(user.name, 'teacher1')

    def test_user_has_name_as_first_name_last_name(self):
        """Animals that can speak are correctly identified"""
        user = User.objects.get(username="teacher2")
        self.assertEqual(user.name, 'first last')

    def test_string_representation(self):
        user = User.objects.get(username="teacher2")
        self.assertEqual(str(user), 'teacher2')
