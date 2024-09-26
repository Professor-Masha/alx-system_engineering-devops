#!/usr/bin/python3

"""
Script to gather employee TODO list progress from a REST API and export
to CSV format.
"""

import csv
import sys
import requests


def export_todo_to_csv(employee_id):
    """Fetch and export TODO data for a given employee ID to CSV."""
    # API endpoint for users and todos
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODOs for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Get the employee username
    username = user_data.get('username', 'Unknown User')

    # Prepare CSV filename
    csv_filename = f"{employee_id}.csv"

    # Write to CSV file
    with open(csv_filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            csv_writer.writerow([
                employee_id,
                username,
                todo['completed'],
                todo['title']
            ])

    print(f"Exported data to {csv_filename}")


if __name__ == "__main__":
    # Check if the user provided an employee ID as an argument
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    # Get employee ID from command line argument
    emp_id = int(sys.argv[1])
    export_todo_to_csv(emp_id)
