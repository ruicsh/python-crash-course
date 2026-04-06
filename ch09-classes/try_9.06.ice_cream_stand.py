class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} is a {self.type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is open.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, "ice cream stand")
        self.flavors = flavors

    def list_flavors(self):
        for flavor in self.flavors:
            print(flavor)


ice_cream_stand = IceCreamStand("Poppy", ["chocolate", "vanilla", "banana"])

ice_cream_stand.list_flavors()
