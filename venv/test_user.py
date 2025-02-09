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


