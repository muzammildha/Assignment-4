import random

def roll_dice():
    user_input = input("Do you want to roll the dice? (y/n): ")
    if user_input.lower() == "y":
        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)

        print(f"You rolled a {dice_roll1} and a {dice_roll2}")

        total = dice_roll1 + dice_roll2

        print(f"The total is {total}")

        user_input2 = input("Do you want to play again? (y/n): ")
        if user_input2.lower() == "y":
            roll_dice()
        else:
            print("Thank you! :)")
    else:
        print("Thank you! :)")

roll_dice()
