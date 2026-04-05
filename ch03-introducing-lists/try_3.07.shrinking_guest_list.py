guest_list = ["Alice", "David", "Charlie"]

guest_list.insert(0, "Adam")
guest_list.insert(2, "Beatrice")
guest_list.append("Daisy")

print(f"{guest_list[0]}, do you want to have dinner with me?")
print(f"{guest_list[1]}, do you want to have dinner with me?")
print(f"{guest_list[2]}, do you want to have dinner with me?")
print(f"{guest_list[3]}, do you want to have dinner with me?")
print(f"{guest_list[4]}, do you want to have dinner with me?")
print(f"{guest_list[5]}, do you want to have dinner with me?")

print("I can only invite two people for dinner")

print(f"{guest_list.pop()}, I can't invite you for dinner")
print(f"{guest_list.pop()}, I can't invite you for dinner")
print(f"{guest_list.pop()}, I can't invite you for dinner")
print(f"{guest_list.pop()}, I can't invite you for dinner")

del guest_list[1]
del guest_list[0]

print(guest_list)
