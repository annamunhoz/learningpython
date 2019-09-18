# Exercise 01: create a python program that takes 2 values
# and then select between sum and sub. Show the result.

print("Submit your first number")
first_number = float(input())

print("Submit your second number")
second_number = float(input())

print("Choose the basic arithmetic: type SUM for sum or SUB for subtraction")
arithmetic = input()

if arithmetic == "SUM":
    print(first_number + second_number)

else:
    print(first_number - second_number)
