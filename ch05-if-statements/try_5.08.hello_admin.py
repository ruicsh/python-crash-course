usernames = ["house12", "admin", "crisis04", "alice_person"]

for username in usernames:
    if username == "admin":
        print(f"Hello {username}, would you like to see a status report")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
