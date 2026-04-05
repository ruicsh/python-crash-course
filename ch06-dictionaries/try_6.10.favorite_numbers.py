favorite_numbers = {
    "alice": [1, 2, 3],
    "bob": [2, 3, 4],
    "charlie": [3, 4, 5],
    "daisy": [4, 5, 6],
    "edna": [5, 6, 7],
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers is {numbers}")
