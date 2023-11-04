#!/usr/bin/python3
"""
Exports user task data to a json file
"""
from requests import get
from json import dump
from sys import argv


def get_data(url):
    """gets data from an api"""
    request = get(url)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(request.status_code)


def main():
    """program starting point"""
    user_id = argv[1]

    # Get user data
    user_data_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    username = get_data(user_data_url)["username"]

    # Get todos
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    todos = get_data(todos_url)

    # Data object to write
    data = {}
    data[user_id] = []

    for todo in todos:
        data[user_id].append({'username': username, 'task': todo['title'], 'completed': todo['completed']})

    with open(f'{user_id}.json', 'w') as f:
        dump(data, f)


if __name__ == "__main__":
    main()
