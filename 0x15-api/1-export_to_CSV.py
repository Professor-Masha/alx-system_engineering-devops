#!/usr/bin/python3
"""Script to export employee TODO list data to CSV format."""

import csv
import requests
import sys

def export_to_csv(employee_id):
    """Fetch employee TODO list data and export to CSV."""
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

    # Prepare CSV file name
    csv_file = f'{employee_id}.csv'

    # Write data to CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, username, task.get('completed'), task.get('title')])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
        export_to_csv(emp_id)
    except ValueError:
        print("Employee ID must be an integer.")
