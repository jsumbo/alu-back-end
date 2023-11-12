#!/usr/bin/python3
"""
Using a REST API, and a given emp_ID, return info about their TODO list.
"""
import requests
import sys


if __name__ == "__main__":
    """ main section """
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/').json()
    EMPLOYEE_NAME = employee.get("name")
    employee_todos = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/todos').json()
    serialized_todos = {}

    for todo in employee_todos:
        serialized_todos.update({todo.get("title"): todo.get("completed")})

    COMPLETED_LEN = len([k for k, v in serialized_todos.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, COMPLETED_LEN, len(serialized_todos)))
    for key, val in serialized_todos.items():
        if val is True:
            print("\t {}".format(key))
