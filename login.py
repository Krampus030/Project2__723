import json

USER_FILE = "user.json"


class User:
    """
    Manage user authentication and balance tracking with persistent storage.
    """

    def __init__(self):
        self.users, self.balances = self.load_users()  # Load user credentials and balances
        self.logged_in_user = None  # Track active session

    def load_users(self):
        """
        Load user data from file and convert balances from 2's complement binary strings to decimal.
        """
        try:
            with open(USER_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                users = data.get("users", {})
                balances = {user: self.twos_complement_to_decimal(int(value, 2)) for user, value in data.get("balances", {}).items()}
                return users, balances
        except (FileNotFoundError, json.JSONDecodeError):
            return {}, {}

    def save_users(self):
        """
        Save current user data, converting balances to 2's complement binary strings.
        """
        data = {
            "users": self.users,
            "balances": {user: format(self.decimal_to_twos_complement(value), '032b') for user, value in self.balances.items()}
        }
        with open(USER_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def decimal_to_twos_complement(self, value, bits=32):
        """
        Convert a decimal integer to 2's complement representation and return as integer.
        """
        return value & (2**bits - 1)

    def twos_complement_to_decimal(self, value, bits=32):
        """
        Convert a 2's complement 32-bit binary integer back to decimal.
        """
        if value & (1 << (bits - 1)):
            return value - (1 << bits)
        return value

    def register(self, username, password, initial_deposit):
        """
        Register a new user with an initial deposit if the username is available.
        """
        if username in self.users:
            print("Error: Username already taken.")
            return False

        if not (8 <= len(password) <= 16):
            print("Error: Password must be between 8 and 16 characters long.")
            return False

        self.users[username] = password
        self.balances[username] = initial_deposit  # Store initial balance
        self.save_users()
        print("Registration successful.")
        return True

    def login(self, username, password):
        """
        Authenticate user and set session.
        """
        if self.users.get(username) == password:
            self.logged_in_user = username
            print(f"Login successful. Welcome, {username}!")
            return True
        print("Error: Invalid username or password.")
        return False

    def logout(self):
        """
        Clear session if a user is logged in.
        """
        if self.logged_in_user:
            print(f"User {self.logged_in_user} logged out.")
            self.logged_in_user = None
        else:
            print("No active user session.")

    def check_balance(self):
        """
        Return the current balance of the logged-in user in decimal format.
        """
        if self.logged_in_user:
            return self.balances.get(self.logged_in_user, 0)
        print("Error: No active session.")
        return None

    def deposit(self, amount):
        """
        Deposit funds into the logged-in user's account.
        """
        if self.logged_in_user:
            self.balances[self.logged_in_user] += amount
            self.save_users()  # Save changes to file
            print(f"Deposited {amount}. New balance: {self.check_balance()}")
        else:
            print("Error: No active session.")

    def withdraw(self, amount):
        """
        Withdraw funds if within the allowed overdraft limit (-1500).
        """
        if self.logged_in_user:
            if self.balances[self.logged_in_user] - amount >= -1500:
                self.balances[self.logged_in_user] -= amount
                self.save_users()  # Save changes to file
                print(f"Withdrawal successful. New balance: {self.check_balance()}")
            else:
                print("Error: Insufficient funds.")
        else:
            print("Error: No active session.")

    def transfer(self, target_user, amount):
        """
        Transfer funds to another user if balance allows.
        """
        if self.logged_in_user:
            if target_user in self.users and self.balances[self.logged_in_user] - amount >= -1500:
                self.balances[self.logged_in_user] -= amount
                self.balances[target_user] += amount
                self.save_users()  # Save changes to file
                print(f"Transfer successful. New balance: {self.check_balance()}")
            else:
                print("Error: Transfer failed.")
        else:
            print("Error: No active session.")


# Global user management instance
user1 = User()
