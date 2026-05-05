# Variables
x = 10
name = "Dipinder"

print(x)
print(name)


# Multiple variables
a = 5
b = 10

sum = a + b
print(sum)


# Data types
x = 10
y = 3.14
name = "John"

print(type(x))
print(type(y))
print(type(name))


# String example
message = "Hello World"
print(message)


# String concatenation
first = "Hello"
second = "World"

print(first + " " + second)


# String slicing
text = "Hello World"

print(text[0:5])


# String formatting (f-string)
name = "Dipinder"
age = 20

print(f"My name is {name} and I am {age} years old")


# Integer operations
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# Float example
price = 23.56
tax_rate = 0.07

total_price = price + (price * tax_rate)
print(total_price)


# Float precision issue
print(0.1 + 0.2)


# Fix precision
print(round(0.1 + 0.2, 2))


# Assignment operator
x = 5
x += 2

print(x)


# Comparison operators
a = 10
b = 5

print(a == b)
print(a > b)
print(a < b)


# Logical operators
x = 10

print(x > 5 and x < 15)
print(x > 5 or x > 20)
print(not(x > 5))


# Local variable
def my_function():
    x = 10
    print(x)

my_function()


# Global variable
x = 10

def my_function():
    global x
    x += 5

my_function()
print(x)

