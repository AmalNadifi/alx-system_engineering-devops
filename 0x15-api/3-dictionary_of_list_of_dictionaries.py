#!/usr/bin/python3
"""
The following script exports to-do list info of all employees to JSON format
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            } for td in requests.get(url + "todos_reponse",
                                     params={"userId": user.get("id")}).json()
            ] for user in users}, jsonfile)
