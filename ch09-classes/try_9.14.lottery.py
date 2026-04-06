import random


digits = [f"{digit}" for digit in range(0, 10)]
letters = [f"{chr(code)}" for code in range(97, 103)]
series = digits + letters


lottery = "".join([random.choice(series) for _ in range(4)]).upper()
print(f"Lottery winner: {lottery}")
