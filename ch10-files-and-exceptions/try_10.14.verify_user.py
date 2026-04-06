from pathlib import Path
import json


def get_stored_username():
    """Get stored username if available."""
    path = Path("username.json")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_username()
    if username:
        this_username = input("What is your username? ")
        if this_username != username:
            get_new_username(path)
        else:
            print(f"Welcome back, {username}")
    else:
        get_new_username(path)
        print(f"We'll remember you when you come back, {username}")


greet_user()
