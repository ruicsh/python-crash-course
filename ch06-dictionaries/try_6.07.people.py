people = [
    {"first_name": "John", "last_name": "Doe", "age": 25, "city": "Tokyo"},
    {"first_name": "Jane", "last_name": "Doe", "age": 23, "city": "Sydney"},
    {"first_name": "Rory", "last_name": "Person", "age": 53, "city": "London"},
]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}".title()
    print(f"{full_name}, aged {person['age']}, from {person['city']}")
