class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} is a {self.type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is open.")

    def set_number_served(self, n):
        if n >= self.number_served:
            self.number_served = n
        else:
            print("Can't decrement the number of clients served.")

    def increment_number_served(self, n):
        self.number_served += n


restaurant = Restaurant("Joe's", "italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"{restaurant.describe_restaurant()} served {restaurant.number_served} clients.")

restaurant.number_served = 2
print(f"{restaurant.describe_restaurant()} served {restaurant.number_served} clients.")

restaurant.set_number_served(5)
print(f"{restaurant.describe_restaurant()} served {restaurant.number_served} clients.")

restaurant.increment_number_served(20)
print(f"{restaurant.describe_restaurant()} served {restaurant.number_served} clients.")
