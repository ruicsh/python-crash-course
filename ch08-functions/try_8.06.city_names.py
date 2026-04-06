def city_country(name, country):
    s = f"{name}, {country}"
    return s.title()


print(city_country("london", "united kingdom"))
print(city_country("tokyo", "japan"))
print(city_country("new york", "united states"))
