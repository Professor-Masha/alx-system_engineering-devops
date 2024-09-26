#!/usr/bin/python3
"""Script to export employee TODO list data to JSON format."""

import json
import requests
import sys

def export_to_json(employee_id):
    """Fetch employee TODO list data and export to JSON."""
    # API URLs
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username', 'Unknown User')

    # Fetch TODO data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare the JSON data structure
    json_data = {
        str(employee_id): [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            } for task in todos_data
        ]
    }

    # Write data to JSON file
    json_file = f'{employee_id}.json'
    with open(json_file, mode='w') as file:
        json.dump(json_data, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
        export_to_json(emp_id)
    except ValueError:
        print("Employee ID must be an integer.")
