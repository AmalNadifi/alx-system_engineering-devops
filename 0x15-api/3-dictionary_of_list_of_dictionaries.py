#!/usr/bin/python3
"""
The following script exports to-do list info of all employees to JSON format
"""

import json
import requests


def fetch_user_info(user_id):
    """
    Fetch user information based on user_id.

    Args:
    - user_id (int): The ID of the user.

    Returns:
    - dict: User information in JSON format.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    return response.json()


def fetch_todo_list(user_id):
    """
    Fetch TODO list for a given user_id.

    Args:
    - user_id (int): The ID of the user.

    Returns:
    - list: List of TODO items for the user in JSON format.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id}
    response = requests.get(url, params=params)
    return response.json()


def export_all_to_json():
    """
    Export to-do list of all employees to JSON.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    data = {
        user["id"]: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            } for todo in fetch_todo_list(user["id"])
        ] for user in users
    }

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    try:
        export_all_to_json()
        print("Data exported to todo_all_employees.json")
    except requests.RequestException as error:
        print(f"Error: {error}")
