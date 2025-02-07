from login import user1
from app import PreAccountCLI
from app import PostAccountCLI


class CLIApp:
    """Command-line application for user authentication."""

    def __init__(self):
        self.user = user1
        self.pre_account_cli = PreAccountCLI(self.user)
        self.post_account_cli = PostAccountCLI(self.user)

    def run(self):
        """Interactive CLI loop for handling user commands."""
        while True:
            command_set = self.post_account_cli if self.user.logged_in_user else self.pre_account_cli

            command_name = input("Enter command: ").strip()

            command = command_set.commands.get(command_name)

            if command:
                command()
            else:
                print(f"Error: Unknown command '{command_name}'.")
                print("Use 'help' to see available commands.")


if __name__ == "__main__":
    app = CLIApp()
    app.run()
