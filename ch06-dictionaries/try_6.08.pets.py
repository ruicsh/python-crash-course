pets = [
    {"animal": "dog", "owner": "Alice"},
    {"animal": "cat", "owner": "Bob"},
    {"animal": "bird", "owner": "Charlie"},
]

for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['animal']}")
