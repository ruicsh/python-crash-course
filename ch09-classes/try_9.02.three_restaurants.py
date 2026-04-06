class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is a {self.type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is open.")


italian = Restaurant("Joe's", "italian")
chinese = Restaurant("Ching", "chinese")
thai = Restaurant("Phong", "thai")

restaurants = [italian, chinese, thai]
for restaurant in restaurants:
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
