# Create a dictionary
student = {"name": "Dipinder", "age": 20}
print(student)


# Access value
print(student["name"])


# Add new key-value pair
student["course"] = "IT"
print(student)


# Modify value
student["age"] = 21
print(student)


# Remove key-value pair
del student["age"]
print(student)


# Using get() method
student = {"name": "Dipinder", "course": "IT"}

print(student.get("name"))
print(student.get("age", "Not found"))


# Loop through dictionary (keys and values)
student = {"name": "Dipinder", "age": 20}

for key, value in student.items():
    print(key, value)


# Loop through keys
for key in student.keys():
    print(key)


# Loop through values
for value in student.values():
    print(value)


# Dictionary of similar objects
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

print(favorite_languages["sarah"])


# Loop with sorted keys
for name in sorted(favorite_languages.keys()):
    print(name)


# Unique values using set()
for language in set(favorite_languages.values()):
    print(language)


# List of dictionaries (nesting)
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# Generate list of dictionaries using loop
aliens = []

for i in range(5):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

print(aliens)


# Modify first few dictionaries
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

print(aliens)


# Dictionary with list inside
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

print(pizza["crust"])

for topping in pizza["toppings"]:
    print(topping)


# Dictionary inside dictionary
users = {
    "user1": {"name": "Dipinder", "age": 20},
    "user2": {"name": "Alex", "age": 22}
}

for username, user_info in users.items():
    print(username)
    print(user_info["name"], user_info["age"])