import random


class Lottery:
    def __init__(self):
        digits = [f"{digit}" for digit in range(0, 10)]
        letters = [f"{chr(code)}" for code in range(97, 103)]
        self.series = digits + letters

    def draw(self):
        return "".join([random.choice(self.series) for _ in range(4)]).upper()


lottery = Lottery()
winning_ticket = lottery.draw()

n_attempts = 0
is_winning_ticket = False
while not is_winning_ticket:
    n_attempts += 1
    my_ticket = lottery.draw()
    is_winning_ticket = my_ticket == winning_ticket

print(f"It took {n_attempts} attempts to win the lottery.")
