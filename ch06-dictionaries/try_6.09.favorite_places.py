favorite_places = {
    "alice": ["london", "sheffield", "manchester"],
    "bob": ["new york", "los angeles", "chicago"],
    "charlie": ["paris", "marseille", "lille"],
}

for name, cities in favorite_places.items():
    cities = [city.title() for city in cities]
    print(f"{name.title()} loves {cities}.")
