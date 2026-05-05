def input_name():
    name = input("Enter your name: ")
    print("Hello", name)


def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            print("Young")
        else:
            print("Adult")
    except:
        print("Invalid input")


def even_odd():
    try:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except:
        print("Invalid input")


def count_loop():
    x = 1
    while x <= 5:
        print(x)
        x += 1


def quit_loop():
    message = input("Enter message (type quit to stop): ")
    while message != "quit":
        print(message)
        message = input("Enter message (type quit to stop): ")


def flag_loop():
    active = True
    while active:
        msg = input("Enter message: ")
        if msg == "quit":
            active = False
        else:
            print(msg)


def break_loop():
    while True:
        try:
            num = int(input("Enter number (even to stop): "))
            if num % 2 == 0:
                break
            else:
                print("Odd number:", num)
        except:
            print("Invalid input")


def continue_loop():
    while True:
        try:
            num = int(input("Enter number (negative to stop): "))
            if num < 0:
                break
            if num % 2 == 0:
                continue
            print("Odd:", num)
        except:
            print("Invalid input")


def list_search():
    animals = ["dog", "cat", "rabbit", "hen"]
    i = 0
    while i < len(animals):
        if animals[i] == "hen":
            print("Found at index", i)
            break
        i += 1


def remove_items():
    pets = ["dog", "cat", "dog", "cat"]
    while "cat" in pets:
        pets.remove("cat")
    print(pets)


def dictionary_input():
    responses = {}
    while True:
        name = input("Enter name: ")
        answer = input("Favourite place: ")
        responses[name] = answer

        repeat = input("Add another? (yes/no): ")
        if repeat == "no":
            break

    print(responses)


# -------------------------------
# MENU SYSTEM
# -------------------------------
while True:
    print("\n--- MENU ---")
    print("1. Enter Name")
    print("2. Check Age")
    print("3. Even/Odd")
    print("4. Count 1-5")
    print("5. Quit Loop")
    print("6. Flag Loop")
    print("7. Break Example")
    print("8. Continue Example")
    print("9. Search List")
    print("10. Remove Items")
    print("11. Dictionary Input")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        input_name()
    elif choice == "2":
        check_age()
    elif choice == "3":
        even_odd()
    elif choice == "4":
        count_loop()
    elif choice == "5":
        quit_loop()
    elif choice == "6":
        flag_loop()
    elif choice == "7":
        break_loop()
    elif choice == "8":
        continue_loop()
    elif choice == "9":
        list_search()
    elif choice == "10":
        remove_items()
    elif choice == "11":
        dictionary_input()
    elif choice == "0":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")