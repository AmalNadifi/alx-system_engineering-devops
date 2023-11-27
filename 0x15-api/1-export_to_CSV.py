import csv
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


def export_to_csv(employee_id, user_name, tasks):
    """Export tasks to a CSV file."""
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            )
        for task in tasks:
            writer.writerow([
                employee_id, user_name, str(task['completed']), task['title']]
                )
    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = sys.argv[1]

        # Fetch user info & Todo list using gather_data_from_an_API.py func
        user_data = fetch_user_info(employee_id)
        user_name = user_data.get("name")
        todo_data = fetch_todo_list(employee_id)

        # Export to CSV
        export_to_csv(employee_id, user_name, todo_data)
