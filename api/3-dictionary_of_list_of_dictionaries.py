#!/usr/bin/python3
"""
Retrieves employee tasks from an API and exports data in JSON format.
"""
import json
import requests


def get_employee_tasks(employee_id):
    """
    Fetches tasks for a specific employee from the API.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_info = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_username = user_info["username"]

    todos_url = f"{base_url}/users/{employee_id}/todos"
    todos_info = requests.get(todos_url).json()

    return [
        {
            "username": employee_username,
            "task": task["title"],
            "completed": task["completed"],
        }
        for task in todos_info
    ]


def get_all_employee_ids():
    """
    Fetches all employee IDs available in the API.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    users_info = requests.get(base_url).json()
    ids = [user["id"] for user in users_info]
    return ids


if __name__ == '__main__':
    all_employee_ids = get_all_employee_ids()

    with open('todo_all_employees.json', "w") as json_file:
        all_employees_tasks = {}
        for emp_id in all_employee_ids:
            all_employees_tasks[str(emp_id)] = get_employee_tasks(emp_id)
        json_file.write(json.dumps(all_employees_tasks, indent=4))
