# Session 8 Complete Program

from pathlib import Path
import json

while True:

    print("\n===== SESSION 8 MENU =====")
    print("1. Read File")
    print("2. Write File")
    print("3. ZeroDivisionError")
    print("4. FileNotFoundError")
    print("5. JSON Write")
    print("6. JSON Read")
    print("7. Save Username")
    print("8. Welcome User")
    print("9. Exit")

    choice = input("Enter choice: ")

    # Part 1
    if choice == "1":
        path = Path("programming.txt")

        if path.exists():
            contents = path.read_text()
            print(contents)
        else:
            print("File not found")

    # Part 2
    elif choice == "2":
        path = Path("programming.txt")

        contents = "I love programming.\n"
        contents += "I love Python.\n"

        path.write_text(contents)

        print("File written successfully")

    # Part 3
    elif choice == "3":
        try:
            answer = 10 / 0
        except ZeroDivisionError:
            print("You cannot divide by zero!")

    # Part 4
    elif choice == "4":
        path = Path("unknown.txt")

        try:
            contents = path.read_text()
        except FileNotFoundError:
            print("File does not exist!")

    # Part 5
    elif choice == "5":
        numbers = [2, 3, 5, 7, 11]

        path = Path("numbers.json")

        contents = json.dumps(numbers)

        path.write_text(contents)

        print("JSON file created")

    # Part 6
    elif choice == "6":
        path = Path("numbers.json")

        if path.exists():
            contents = path.read_text()

            numbers = json.loads(contents)

            print(numbers)
        else:
            print("numbers.json not found")

    # Part 7
    elif choice == "7":
        username = input("Enter your name: ")

        path = Path("username.json")

        contents = json.dumps(username)

        path.write_text(contents)

        print("Username saved")

    # Part 8
    elif choice == "8":
        path = Path("username.json")

        if path.exists():
            contents = path.read_text()

            username = json.loads(contents)

            print("Welcome back,", username)
        else:
            print("No username stored")

    # Part 9
    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")