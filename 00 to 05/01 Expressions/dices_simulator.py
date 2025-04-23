import random

def dices():
    for _ in range(3):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Roll: {die1}, {die2}")

dices()
    
        