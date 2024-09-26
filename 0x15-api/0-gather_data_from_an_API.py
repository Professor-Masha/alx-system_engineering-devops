#!/usr/bin/python3

"""
Script to gather employee TODO list progress from a REST API.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """Fetch and display TODO progress for a given employee ID."""
    # API endpoint for users and todos
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODOs for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate completed tasks
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    total_tasks = len(todos_data)
    completed_count = len(completed_tasks)

    # Employee name
    employee_name = user_data.get('name', 'Unknown User')

    # Print output
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    # Check if the user provided an employee ID as an argument
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get employee ID from command line argument
    emp_id = int(sys.argv[1])
    get_employee_todo_progress(emp_id)
