results = {}

while True:
    name = input("What is your name? ")
    if name == "quit":
        break

    vacation = input("What is your dream vacation? ")
    results[name] = vacation

for name, vacation in results.items():
    print(f"{name.title()} would like to go to {vacation.title()}")
