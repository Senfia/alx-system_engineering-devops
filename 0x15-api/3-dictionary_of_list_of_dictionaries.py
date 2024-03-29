#!/usr/bin/python3
""" This module using the given REST API, for a given employee ID,
exports data in the JSON format. Records all tasks from all employees"""

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    res = requests.get(user)
    json_ot = res.json()
    d_task = {}
    for user in json_ot:
        name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(url, userid)
        res = requests.get(todos)
        tasks = res.json()
        t_task = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            t_task.append(dict_task)

        d_task[str(userid)] = t_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
