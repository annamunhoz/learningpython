# Create a program to act like some dice
# Take input that says how many sides the dice should have
# Output the dice roll

import random

print("Let's roll some dices! Type how many sides your dice has:")
sizes_dice = int(input())

def roll_dices():
    number = random.randint(1,sizes_dice)
    print("Your number is {}".format(number))
    return number

roll_dices()
