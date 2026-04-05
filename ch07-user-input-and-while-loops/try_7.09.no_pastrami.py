sandwich_orders = [
    "blt",
    "pastrami",
    "chicken",
    "pastrami",
    "pastrami",
    "salame",
    "tuna",
    "turkey",
]

print("\nThe deli has run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

finished_sandwiches = []
orders = sandwich_orders[:]
for sandwich in orders:
    print(f"I made a {sandwich} sandwich.")
    sandwich_orders.remove(sandwich)
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
