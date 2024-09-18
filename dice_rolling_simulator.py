import random

def roll_dice(rolls):
    for _ in range(rolls):
        roll = random.randint(1,6)
        print(f"Rolled a {roll}")

number_of_rolls = 5
roll_dice(number_of_rolls)