#!/usr/bin/python3
"""
Exports user task data to a csv file
"""
from requests import get
from json import dump


def get_data(url):
    """gets data from an api"""
    request = get(url)

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(request.status_code)


def main():
    """program starting point"""
    # Get users
    users_data_url = 'https://jsonplaceholder.typicode.com/users'
    users = get_data(users_data_url)

    # Check if all users are found
    all_users_found = all('id' in user for user in users)
    if all_users_found:
        print("All users found: OK")
    else:
        print("All users found: Error")

    # Create a user hashmap for faster lookup
    users_hashmap = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        users_hashmap[user_id] = username

    # Get todos
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos = get_data(todos_url)

    # Data object to write
    data = {}

    # Add todos to data object
    for todo in todos:
        user_id = todo["userId"]
        task_data = {'username': users_hashmap[user_id], 'task': todo['title'], 'completed': todo['completed']}

        if user_id not in data:
            data[user_id] = []
        
        data[user_id].append(task_data)

    with open('todo_all_employees.json', 'w') as f:
        dump(data, f)

    # Check if the user ID and tasks output is correct
    correct_output = all(data[str(user['id'])] for user in users)
    if correct_output:
        print("User ID and Tasks output: OK")
    else:
        print("User ID and Tasks output: Error")


if __name__ == "__main__":
    main()
