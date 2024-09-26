#!/usr/bin/python3
"""Script to gather TODO list progress of an employee."""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetch employee TODO list progress from API."""
    # API URLs
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown Employee')

    # Fetch TODO data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    done_tasks_count = len(done_tasks)

    # Print results
    print(f'Employee {employee_name} is done with tasks({done_tasks_count}/{total_tasks}):')
    for task in done_tasks:
        print(f'\t {task.get("title")}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
        get_employee_todo_progress(emp_id)
    except ValueError:
        print("Employee ID must be an integer.")
