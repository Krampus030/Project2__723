import unittest
import os
import json
from login import User  # Assuming the User class is in login.py

USER_TEST_FILE = "test_user.json"

class TestUser(unittest.TestCase):
    """
    Unit test cases for the User class.
    """

    def setUp(self):
        """
        Set up a test User instance with mocked storage methods.
        """
        self.user = User()
        self.user.users = {}  # Clear user data
        self.user.balances = {}  # Clear balances
        self.user.logged_in_user = None  # Reset session
        self.user.save_users = self.mock_save_users  # Mock the save method
        self.user.load_users = self.mock_load_users  # Mock the load method

    def mock_save_users(self):
        """
        Mock saving user data by storing it in memory.
        """
        self.mock_data = {
            "users": self.user.users,
            "balances": self.user.balances
        }

    def mock_load_users(self):
        """
        Mock loading user data by retrieving it from memory.
        """
        return self.mock_data.get("users", {}), self.mock_data.get("balances", {})

    def test_register(self):
        """
        Verify a user can register successfully.
        """
        result = self.user.register("k", "11111111", 1500)
        self.assertTrue(result)  # Registration should succeed
        self.assertIn("k", self.user.users)  # User should be stored
        self.assertEqual(self.user.balances["k"], 1500)  # Initial deposit should match

    def test_register_duplicate_user(self):
        """
        Ensure duplicate usernames can't be registered.
        """
        self.user.register("k", "11111111", 1500)
        result = self.user.register("k", "22222222", 1600)
        self.assertFalse(result)  # Duplicate registration should fail
        self.assertEqual(self.user.balances["k"], 1500)  # Balance should remain unchanged

    def test_login(self):
        """
        Check user login with valid credentials.
        """
        self.user.register("k", "11111111", 1600)
        result = self.user.login("k", "11111111")
        self.assertTrue(result)  # Login should succeed
        self.assertEqual(self.user.logged_in_user, "k")  # Session should track the logged-in user
