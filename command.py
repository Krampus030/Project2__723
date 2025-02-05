from login import User


class Command:
    def __init__(self):
        self.user = User()

    def execute(self, args):
        raise NotImplementedError("Child class must have execute method")


class HelpCommand(Command):
    def execute(self, args):
        print("Available command:")
        print("help     show all commands")



class Register(Command):
    def execute(self, **kwargs):
        username = input("Enter user name:\n")
        password = input("Enter password:\n")
        self.user.register(username, password)


class Login(Command):
    def execute(self, **kwargs):
        username = input("Enter user name:\n")
        password = input("Enter password:\n")
        self.user.login(username, password)


command1 = Login()
command1.execute()
