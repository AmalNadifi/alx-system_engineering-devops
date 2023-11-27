#!/usr/bin/python3
""" The following script is using the given REST API,
for a given employee ID, returns information about his/her TODO list progress
"""
import requests
import sys


def fetch_user_info(employee_id):
    """Fetch user information based on employee_id."""
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    return user_response.json()


def fetch_todo_list(employee_id):
    """Fetch TODO list for a given employee_id."""
    url = "https://jsonplaceholder.typicode.com/"
    todo_response = requests.get(url + "todos", params={"userId": employee_id})
    return todo_response.json()


def display_todo_progress(employee_name, completed_tasks, total_tasks):
    """Display TODO list progress on standard output."""
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))
    [print("\t {}".format(task)) for task in completed_tasks]


if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")

    else:
        # Convert command-line argument to an integer
        employee_id = int(sys.argv[1])

        # Fetch user info
        user_data = fetch_user_info(employee_id)
        employee_name = user_data.get("name")

        # Fetch TODO list
        todo_data = fetch_todo_list(employee_id)

        # Filter completed tasks
        completed_tasks = [
                task.get("title") for task in todo_data
                if task.get("completed")
                ]

        # Display results
        display_todo_progress(employee_name, completed_tasks, len(todo_data))
