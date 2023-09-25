#!/usr/bin/python3
"""
This module using the given REST API, for a given employee ID,
exports data in the CSV format
"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user = '{}users/{}'.format(url, user_id)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?user_id={}'.format(url, user_id)
    res = requests.get(todos)
    tasks = res.json()
    t_task = []
    for task in tasks:
        t_task.append([user_id,
                       name,
                       task.get('completed'),
                       task.get('title')])

    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in t_task:
            employee_writer.writerow(task)
