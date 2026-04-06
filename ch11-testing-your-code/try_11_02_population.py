from city_functions import city_country


def test_city_country():
    assert city_country("santiago", "chile") == "Santiago, Chile"


def test_city_country_population():
    s = city_country("santiago", "chile", 10_000_000)
    assert s == "Santiago, Chile - population: 10000000"
