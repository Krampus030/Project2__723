import json

user_file = "user.json"


class User:
    """
    Manage user registration, login, and logout.
    Store user credentials in a JSON file for persistence.
    """
    def __init__(self):
        self.users = self.load_users()  # Load existing users
        self.logged_in_user = None  # Track the current user session

    def load_users(self):
        """
        oad user data from file, return empty dict if file is missing or invalid
        ."""
        try:
            with open(user_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self):
        """
        Save current user data to file.
        """
        with open(user_file, "w") as f:
            json.dump(self.users, f, indent=4)

    def register(self, username, password):
        """
        Register new user if username is not taken.
        """
        if username in self.users:
            print("This user name has been used.")
            return False

        self.users[username] = password
        self.save_users()
        print("Register success!")
        return True

    def login(self, username, password):
        """
        Authenticate user credentials and set session.
        """
        if username in self.users and self.users[username] == password:
            self.logged_in_user = username
            print(f"Login success! Welcome, {username}!")
            return True
        else:
            print("Incorrect username or password")
            return False

    def logout(self):
        """
        Clear current session if a user is logged in.
        """
        if self.logged_in_user:
            print(f"User {self.logged_in_user} logged out.")
            self.logged_in_user = None
        else:
            print("There is no user logged in.")
