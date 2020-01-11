# Like exercise 03, but extended to allow the user to input how many dice they'd like to roll
# Roll and output each dice
# If the number of dice is greater than 1, output the total of all the dice

import random

print("Let's roll some dices! Type how many dices do you want to roll:")
quantity_dices = int(input())

print("Type how many sides your dices has:")
sizes_dice = int(input())


def roll_dice(quantity_dices):
    number = random.randint(1, sizes_dice)
    return number


def roll_dices(quantity_dices):
    sum_dices = 0
    for i in range(quantity_dices):
        rolled_dice = roll_dice(quantity_dices)
        sum_dices += rolled_dice
        print("Dice {} is number {}".format(i+1,rolled_dice))
    if quantity_dices > 1:
        print("The sum is {}".format(sum_dices))


roll_dices(quantity_dices)
