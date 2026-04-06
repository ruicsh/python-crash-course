def city_country(city, country, population=None):
    if not population:
        return f"{city}, {country}".title()
    else:
        return f"{city.title()}, {country.title()} - population: {population}"
