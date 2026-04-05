guest_list = ["Alice", "Bob", "Charlie"]

cant_make_it = "Bob"
print(cant_make_it)

guest_list.remove(cant_make_it)
guest_list.append("David")

print(f"{guest_list[0]}, do you want to have dinner with me?")
print(f"{guest_list[1]}, do you want to have dinner with me?")
print(f"{guest_list[2]}, do you want to have dinner with me?")
