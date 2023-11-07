#!/usr/bin/python3
"""
Exports user task data to a JSON file
"""
import requests
from json import dump


def get_data(url):
    """Gets data from an API"""
    response = requests.get(url)
    response.raise_for_status()  # Raises an exception for 4xx/5xx status codes
    return response.json()


def fetch_user_data():
    """Fetches user data from the API"""
    users_data_url = 'https://jsonplaceholder.typicode.com/users'
    return get_data(users_data_url)


def fetch_todo_data():
    """Fetches todo data from the API"""
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    return get_data(todos_url)


def export_data_to_json(data, filename):
    """Exports data to a JSON file"""
    with open(filename, 'w') as file:
        dump(data, file)


def main():
    """Program starting point"""
    try:
        users = fetch_user_data()

        # Check if all users are found
        all_users_found = all('id' in user for user in users)
        if all_users_found:
            print("All users found: OK", end="")
        else:
            print("All users found: Error", end="")

        # Create a user hashmap for faster lookup
        users_hashmap = {user['id']: user['username'] for user in users}

        todos = fetch_todo_data()

        # Data object to write
        data = {}

        # Add todos to data object
        for todo in todos:
            user_id = todo["userId"]
            task_data = {
                'username': users_hashmap[user_id],
                'task': todo['title'],
                'completed': todo['completed']
            }

            if user_id not in data:
                data[user_id] = []

            data[user_id].append(task_data)

        export_data_to_json(data, 'todo_all_employees.json')

        # Check if the user ID and tasks output is correct
        correct_output = all(data[str(user['id'])] for user in users)
        if correct_output:
            print("User ID and Tasks output: OK")
        else:
            print("User ID and Tasks output: Error")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
