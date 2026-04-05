current_users = ["house12", "admin", "crisis04", "alice_person", "john20"]
new_users = ["crisis04", "JOHN20"]

current_users_lower = [username.lower() for username in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}, please create a new username.")
    else:
        print(f"{new_user} is available.")
