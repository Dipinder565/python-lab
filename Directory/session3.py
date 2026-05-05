# List example
fruits = ["apple", "banana", "orange"]
print(fruits)


# Accessing list elements
print(fruits[0])
print(fruits[1])
print(fruits[-1])


# Modifying list elements
fruits[1] = "mango"
print(fruits)


# Adding item using append()
fruits.append("grapes")
print(fruits)


# Adding item using insert()
fruits.insert(1, "kiwi")
print(fruits)


# Removing item using del
del fruits[0]
print(fruits)


# Removing item using pop()
removed_item = fruits.pop()
print(fruits)
print(removed_item)


# Removing item using remove()
fruits.remove("mango")
print(fruits)


# Sorting list permanently
numbers = [15, 5, 30, 25, 10]
numbers.sort()
print(numbers)


# Sorting list temporarily
numbers = [15, 5, 30, 25, 10]
sorted_numbers = sorted(numbers)

print(sorted_numbers)
print(numbers)


# Sorting in reverse order
numbers = [15, 5, 30, 25, 10]
numbers.sort(reverse=True)
print(numbers)


# Reversing list order
fruits = ["apple", "banana", "orange", "berry"]
fruits.reverse()
print(fruits)


# List length
numbers = [1, 2, 3, 4, 5]
print(len(numbers))


# For loop through list
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)


# For loop with message
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")


# Code after loop
for magician in magicians:
    print(magician)

print("Thank you, everyone.")


# Range function
for value in range(1, 5):
    print(value)


# Range with different start and stop
for i in range(2, 6):
    print(i)


# Loop through a string
word = "Program"

for ch in word:
    print(ch)


# Loop through string using index
my_string = "Hello"

for i in range(len(my_string)):
    print(f"Index {i}: {my_string[i]}")


# Index error example
names = ["John", "George", "Josh"]

print(names[0])
print(names[1])
print(names[2])
# print(names[3])  # This gives IndexError


# Tuple example
my_tuple = (1, 2, 3)
print(my_tuple)


# Access tuple element
print(my_tuple[0])


# Single element tuple
single_element_tuple = (1,)
print(single_element_tuple)


# Tuple unpacking
a, b, c = my_tuple

print(a)
print(b)
print(c)


# Tuple loop
for item in my_tuple:
    print(item)


# Tuple slicing
sub_tuple = my_tuple[1:3]
print(sub_tuple)