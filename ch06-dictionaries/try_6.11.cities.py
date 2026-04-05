cities = {
    "london": {"country": "united kingdom", "population": 8_866_000},
    "tokyo": {"country": "japan", "population": 14_250_000},
    "new york": {"country": "united states", "population": 8_478_000},
}

for city, info in cities.items():
    print(
        f"{city.title()}, {info['country'].title()} with a population of {info['population']}"
    )
