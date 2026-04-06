import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


dice_6_side = Die()
dice_10_side = Die(10)
dice_20_side = Die(20)
for _ in range(11):
    dice_6_side.roll_die()
    dice_10_side.roll_die()
    dice_20_side.roll_die()
