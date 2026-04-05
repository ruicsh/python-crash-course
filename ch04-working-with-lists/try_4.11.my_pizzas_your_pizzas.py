pizzas = ["Margherita", "New York", "Pepperoni"]
friend_pizzas = pizzas[:]

pizzas.append("Four Cheeses")
friend_pizzas.append("Meat Feast")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
