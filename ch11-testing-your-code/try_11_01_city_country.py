from city_functions import city_country


def test_city_country():
    assert city_country("santiago", "chile") == "Santiago, Chile"
