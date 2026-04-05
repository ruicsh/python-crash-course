sandwich_orders = ["blt", "chicken", "salame", "tuna", "turkey"]

finished_sandwiches = []
orders = sandwich_orders[:]
for sandwich in orders:
    print(f"I made a {sandwich} sandwich.")
    sandwich_orders.remove(sandwich)
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
