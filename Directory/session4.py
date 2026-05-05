# Basic if statement
x = 10

if x > 5:
    print("Greater than 5")


# If-else example
x = 4

if x > 5:
    print("Greater")
else:
    print("Smaller")


# If-elif-else example
age = 20

if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")


# Even or odd number
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Multiple if conditions (independent)
toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in toppings:
    print("Adding mushrooms")

if "extra cheese" in toppings:
    print("Adding extra cheese")


# If inside loop
toppings = ["mushrooms", "green peppers", "extra cheese"]

for topping in toppings:
    if topping == "green peppers":
        print("Sorry, we are out of green peppers")
    else:
        print(f"Adding {topping}")


# Check empty list
toppings = []

if toppings:
    for topping in toppings:
        print(f"Adding {topping}")
else:
    print("Are you sure you want a plain pizza?")


# Input validation example
available_toppings = ["mushrooms", "olives", "green peppers", "extra cheese"]
requested_toppings = ["mushrooms", "french fries"]

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}")
    else:
        print(f"Sorry, we don't have {topping}")


# Logical operators
x = 10

if x > 5 and x < 15:
    print("x is between 5 and 15")

if x > 5 or x > 20:
    print("Condition is True")

if not(x > 5):
    print("This will not run")


# Simple condition check
number = 0

if number == 0:
    print("Number is zero")

print("After if code")