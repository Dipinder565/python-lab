# Session 9 Complete Program

import requests

while True:

    print("\n===== SESSION 9 MENU =====")
    print("1. Simple API Call")
    print("2. Check Status Code")
    print("3. Convert API Response to Dictionary")
    print("4. Show Response Keys")
    print("5. GitHub Python Repositories")
    print("6. Show Repository Names")
    print("7. Show Repository Stars")
    print("8. API Rate Limit")
    print("9. Exit")

    choice = input("Enter choice: ")

    # Part 1
    if choice == "1":
        url = "https://api.github.com/search/repositories"
        url += "?q=language:python+sort:stars"

        print(url)

    # Part 2
    elif choice == "2":
        url = "https://api.github.com/search/repositories"
        url += "?q=language:python+sort:stars"

        r = requests.get(url)

        print("Status code:", r.status_code)

    # Part 3
    elif choice == "3":
        url = "https://api.github.com/search/repositories"
        url += "?q=language:python+sort:stars"

        r = requests.get(url)

        response_dict = r.json()

        print(type(response_dict))
        print(response_dict)

    # Part 4
    elif choice == "4":
        url = "https://api.github.com/search/repositories"
        url += "?q=language:python+sort:stars"

        r = requests.get(url)

        response_dict = r.json()

        print(response_dict.keys())

    # Part 5
    elif choice == "5":
        url = "https://api.github.com/search/repositories"
        url += "?q=language:python+sort:stars+stars:>10000"

        headers = {"Accept": "application/vnd.github.v3+json"}

        r = requests.get(url, headers=headers)

        response_dict = r.json()

        print("Total repositories:", response_dict["total_count"])
        print("Complete results:", not response_dict["incomplete_results"])

    # Part 6
    elif choice == "6":
        url = "https://api.github.com/search/repositories"
        url += "?q=language:python+sort:stars+stars:>10000"

        headers = {"Accept": "application/vnd.github.v3+json"}

        r = requests.get(url, headers=headers)

        response_dict = r.json()

        repo_dicts = response_dict["items"]

        for repo_dict in repo_dicts:
            print(repo_dict["name"])

    # Part 7
    elif choice == "7":
        url = "https://api.github.com/search/repositories"
        url += "?q=language:python+sort:stars+stars:>10000"

        headers = {"Accept": "application/vnd.github.v3+json"}

        r = requests.get(url, headers=headers)

        response_dict = r.json()

        repo_dicts = response_dict["items"]

        for repo_dict in repo_dicts:
            print(repo_dict["name"], "-", repo_dict["stargazers_count"])

    # Part 8
    elif choice == "8":
        url = "https://api.github.com/rate_limit"

        r = requests.get(url)

        response_dict = r.json()

        print(response_dict["resources"]["search"])

    # Part 9
    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        