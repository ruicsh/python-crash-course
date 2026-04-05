usernames = ["house12", "admin", "crisis04", "alice_person"]

if len(usernames):
    for username in usernames:
        if username == "admin":
            print(f"Hello {username}, would you like to see a status report")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
