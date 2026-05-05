# -------------------------------
# FUNCTIONS
# -------------------------------

def greet_user():
    print("Hello!")


def greet_name():
    name = input("Enter name: ")
    print("Hello", name)


def describe_pet():
    animal = input("Enter animal: ")
    name = input("Enter pet name: ")
    print("I have a", animal)
    print("My pet name is", name)


def return_name():
    f = input("First name: ")
    l = input("Last name: ")
    print(f + " " + l)


def optional_name():
    f = input("First name: ")
    l = input("Last name: ")
    m = input("Middle name (optional): ")

    if m:
        print(f, m, l)
    else:
        print(f, l)


def dictionary_example():
    name = input("Name: ")
    age = input("Age: ")
    person = {"name": name, "age": age}
    print(person)


def list_function():
    users = ["Dipinder", "Alex", "John"]
    for u in users:
        print("Hello", u)


def pizza():
    print("Enter toppings (type stop to end)")
    toppings = []

    while True:
        t = input("Topping: ")
        if t == "stop":
            break
        toppings.append(t)

    print("Pizza with:")
    for t in toppings:
        print("-", t)


# -------------------------------
# MENU
# -------------------------------

while True:
    print("\n--- SESSION 7 MENU ---")
    print("1. Simple Function")
    print("2. Greet User")
    print("3. Describe Pet")
    print("4. Return Full Name")
    print("5. Optional Name")
    print("6. Dictionary Example")
    print("7. List Function")
    print("8. Pizza (*args concept)")
    print("0. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        greet_user()
    elif choice == "2":
        greet_name()
    elif choice == "3":
        describe_pet()
    elif choice == "4":
        return_name()
    elif choice == "5":
        optional_name()
    elif choice == "6":
        dictionary_example()
    elif choice == "7":
        list_function()
    elif choice == "8":
        pizza()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice")