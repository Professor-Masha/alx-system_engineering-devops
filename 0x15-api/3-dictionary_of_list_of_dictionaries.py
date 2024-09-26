#!/usr/bin/env python3
"""
Export data in JSON format.
"""

import json
import requests

def fetch_data():
    """Fetch data from the API and return it."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    return users, todos

def export_to_json(users, todos):
    """Export data to a JSON file."""
    todo_data = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']
        user_tasks = []

        for task in todos:
            if task['userId'] == user['id']:
                user_tasks.append({
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                })

        todo_data[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_data, json_file)

def main():
    """Main function to fetch data and export it."""
    users, todos = fetch_data()
    export_to_json(users, todos)

if __name__ == "__main__":
    main()
