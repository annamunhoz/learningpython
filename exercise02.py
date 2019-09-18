# Exercise 02: like the exercise 01, but adding multiplication and division
# must be used a function with 3 values: number 1, number 2 and the arithmetic
# list the possibles arithmetics (a letter to each one)
# you can not use else
# the function can have any number of returns needed
# show a error message if the arithmetic doesn't exist

print("Choose your first number")
first_number = float(input())

print("Choose your second number")
second_number = float(input())

print("Choose the arithmetic:"
"A to sum; "
"B to subtraction; "
"C to multiplication; "
"D to division")
arithmetic = input().upper()

def math(first_number,second_number,arithmetic):
# To do the math with the inputs given by the user and/or to show the error message

    if arithmetic == "A":
        return (first_number+second_number)

    if arithmetic == "B":
        return (first_number-second_number)

    if arithmetic == "C":
        return (first_number*second_number)

    if arithmetic == "D":
        return (first_number/second_number)

    return "Ops! The input letter wasn't recognized. Please try again."

result = math(first_number,second_number,arithmetic)
print(result)
