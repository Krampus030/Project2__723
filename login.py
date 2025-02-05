import json
user_file = "user.json"


class User:
    """
    This class is aimed to create, store and check user credentials
    """
    def __init__(self):
        self.users = self.load_users()
        # initialise the file, load existed data

    def load_users(self):
        """
        If file is already exist, open with read mode
        and load the data in dictionary form.

        If not, error handling and return an empty dict.
        :return: exist file or {}
        """
        try:
            with open(user_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self):
        """
        write mode, transfer the python dictionary 'self.users' into json form.
        :return: user input data
        """
        with open(user_file, "w") as f:
            json.dump(self.users, f, indent=4)

    def register(self, username, password):
        if username in self.users:
            print("This user name has been used.")
            return False  # duplicate account handling

        self.users[username] = password
        self.save_users()
        print("Register success!")
        return True  # store the input in a dictionary and call the save method

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Login success")
            return True  # check credentials
        else:
            print("Incorrect username or password")
        # error message
        