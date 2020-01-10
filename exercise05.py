# Higher or lower game
# The computer chooses a random number between 1 and `n` (you choose what `n` is)
# The user then can make guesses at what the number is
# If their guess is correct, it outputs that they win.
# If it is incorrect, it outputs whether the target number is higher or lower than their guess

import random

print("The computer will choose a number between 1 and 100. Type your guess below!")
guess = int(input())


def guess_game(guess):
    number = random.randint(1, 100)
    # print("The computer choose {}".format(number))
    if number == guess:
        print("You won! The number was {}".format(number))
    elif number > guess:
        print("You lose! It was a higher number.")
    else:
        print("You lose! It was a lower number.")


guess_game(guess)
