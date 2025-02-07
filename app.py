class PreAccountCLI:
    """Handles user registration and login commands."""

    def __init__(self, user_instance):
        self.user = user_instance
        self.commands = {
            "register": self.register,
            "login": self.login,
            "help": self.help,
            "logout": self.logout
        }

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password(should between 8 to 16 char): ")
        initial_deposit = int(input("Enter initial deposit: "))
        self.user.register(username, password, initial_deposit)

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.user.login(username, password)

    def logout(self):
        self.user.logout()

    def help(self):
        print("\nAvailable commands:")
        print("  register  - Register a new user")
        print("  login     - Log in to an existing account")
        print("  logout    - Can not log out since not logged in yet")
        print("  help      - Show this help message\n")


class PostAccountCLI:
    """Handles operations available after login."""

    def __init__(self, user_instance):
        self.user = user_instance
        self.commands = {
            "check_balance": self.check_balance,
            "deposit": self.deposit,
            "withdraw": self.withdraw,
            "transfer": self.transfer,
            "logout": self.logout,
            "help": self.help
        }

    def check_balance(self):
        print(f"Balance: {self.user.check_balance()}")

    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        self.user.deposit(amount)

    def withdraw(self):
        amount = int(input("Enter withdrawal amount: "))
        self.user.withdraw(amount)

    def transfer(self):
        target_user = input("Enter target username: ")
        amount = int(input("Enter transfer amount: "))
        self.user.transfer(target_user, amount)

    def logout(self):
        self.user.logout()

    def help(self):
        print("\nAvailable commands:")
        print("  check_balance  - View account balance")
        print("  deposit        - Add money to account")
        print("  withdraw       - Withdraw money")
        print("  transfer       - Transfer money to another user")
        print("  logout         - Log out of the account")
        print("  help           - Show this help message\n")





