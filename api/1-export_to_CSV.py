#!/usr/bin/python3
"""
Using a REST API and an EMP_ID, save info about their TODO list in a csv file
"""
import requests
import sys


if __name__ == "__main__":
    """ main section """
    EMP_ID = sys.argv[1]
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee = requests.get(
        BASE_URL + f'/users/{EMP_ID}/').json()
    EMPLOYEE_NAME = employee.get("username")
    employee_todos = requests.get(
        BASE_URL + f'/users/{EMP_ID}/todos').json()
    serialized_todos = {}

    for todo in employee_todos:
        serialized_todos.update({todo.get("title"): todo.get("completed")})

    COMPLETED_LEN = len([k for k, v in serialized_todos.items() if v is True])
    with open(str(EMP_ID) + '.csv', "w") as f:
        [
            f.write(
                '"' + str(sys.argv[1]) + '",' +
                '"' + EMPLOYEE_NAME + '",' +
                '"' + str(todo["completed"]) + '",' +
                '"' + todo["title"] + '",' + "\n"
            )
            for todo in employee_todos
        ]
