#!/usr/bin/python3
""" THe following script exports data in the CSV format """
import csv
import requests
import sys


if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
    else:
        # Extract employee ID from command-line argument
        employee_id = sys.argv[1]

        # API base URL
        base_url = "https://jsonplaceholder.typicode.com/"

        # Fetch user information
        user_response = requests.get(
                base_url + "users/{}".format(employee_id)).json()
        employee_username = user_response.get("username")

        # Fetch Todo list
        todos_response = requests.get(
                base_url + "todos", params={"userId": employee_id}).json()

        # Export to CSV
        with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            [csv_writer.writerow(
                [employee_id, employee_username,
                    todo.get("completed"), todo.get("title")]
             ) for todo in todos_response]
