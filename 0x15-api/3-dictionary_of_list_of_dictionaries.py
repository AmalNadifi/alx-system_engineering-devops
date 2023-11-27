#!/usr/bin/python3
"""
The following script exports to-do list info of all employees to JSON format
"""

import json
import requests

if __name__ == "__main__":
    # Retrieving user data from the API
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        # Creating a JSON structure with user IDs as keys
        # & associated tasks as values
        json.dump({
            user.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": user.get("id")}).json()
            ] for user in users
        }, jsonfile)
