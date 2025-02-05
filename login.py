import json

user_file = "user.json"


class User:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(user_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self):
        with open(user_file, "w") as f:
            json.dump(self.users, f, indent=4)

    def register(self, username, password):
        if username in self.users:
            print("This user name has been used.")
            return False

        self.users[username] = password
        self.save_users()
        print("Register success!")
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Login success")
            return True
        else:
            print("Incorrect username or password")
