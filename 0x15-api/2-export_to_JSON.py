#!/usr/bin/python3
""" THe following script exports data in the JSON format """
import json
import requests
import sys


if __name__ == "__main__":
    # Checking for the correct number of command-line arguments
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
    else:
        # Extracting employee ID from command-line argument
        employee_id = sys.argv[1]

        # API base URL
        base_url = "https://jsonplaceholder.typicode.com/"

        # Fetching user information
        user_response = requests.get(
                base_url + "users/{}".format(employee_id)).json()
        employee_username = user_response.get("username")

        # Fetch Todo list
        todos_response = requests.get(
                base_url + "todos", params={"userId": employee_id}).json()

        # Exporting to JSON
        with open("{}.json".format(employee_id), "w") as jsonfile:
            json.dump({employee_id: [{
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": employee_username
                } for todo in todos_response]}, jsonfile)
