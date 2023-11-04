#!/usr/bin/python3
"""
Exports user task data to a csv file
"""
from requests import get
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

    # Create text to write
    text = ''
    
    for todo in todos:
        todo_status = todo["completed"]
        todo_title = todo["title"]
        text += f'"{user_id}","{username}","{todo_status}","{todo_title}"\n'

    with open(f'{user_id}.csv', "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
