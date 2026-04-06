def make_car(manufacturer, model, **kwargs):
    car = kwargs
    car["manufacturer"] = manufacturer.title()
    car["model"] = model.title()
    return car


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
