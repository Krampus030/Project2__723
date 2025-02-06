from login import User
import sys


class Command:
    def __init__(self, CLI):
        self.cli = CLI
        self.user = User()

    def execute(self, args):
        raise NotImplementedError("Child class must have execute method")


class Help(Command):

    def execute(self, args):
        if not self.cli.user.logged_in_user:
            print("Error, please login first!")
            return False
        print("Available command:")
        print("  help          Show all commands")
        print("  register      Open a new account")
        print("  login         Login")
        print("  logout        Log out")



class Register(Command):
    def execute(self, args):
        username = input("Enter user name:\n")
        password = input("Enter password:\n")
        self.user.register(username, password)


class Login(Command):
    def execute(self, args):
        username = input("Enter user name:\n")
        password = input("Enter password:\n")
        self.user.login(username, password)


class Logout(Command):
    def execute(self, args):
        if self.cli.user.logged_in_user:
            self.cli.user.logout()
        else:
            print("No user is logged in.")



class CLIApp:
    def __init__(self):
        self.user = User()

        self.commands = {
            "help": Help(self),
            "register": Register(self),
            "login": Login(self),
            "logout": Logout(self)
            # "":
            # "":
            # "":
        }

    def run(self):
        if len(sys.argv) < 2:
            print("Error: Please enter command. For example 'app.py help")
            return

        command_name = sys.argv[1]
        args = sys.argv[2:]

        command = self.commands.get(command_name)

        if command:
            command.execute(args)
        else:
            print(f"Unknown command {command_name}")
            print("Enter app.py help to check available commands")



if __name__ == "__main__":
    app = CLIApp()
    app.run()
