from pathlib import Path
import json


def get_new_user(path):
    """Prompt for a new user."""
    username = input("What is your name? ")
    dob = input("What is your date of birth? ")
    age = int(input("What is your age? "))
    user = {"user": username, "dob": dob, "age": age}
    contents = json.dumps(user)
    path.write_text(contents)


path = Path("user.json")
get_new_user(path)

contents = path.read_text()
user = json.loads(contents)
print(user)
