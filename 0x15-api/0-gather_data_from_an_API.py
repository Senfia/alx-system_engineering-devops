#!/usr/bin/python3
"""
This module using the given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_out = res.json()
    print("Employee {} is done with tasks".format(json_ot.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    t_task = []
    for task in tasks:
        if task.get('completed') is True:
            t_task.append(task)

    print("({}/{}):".format(len(t_task), len(tasks)))
    for task in t_task:
        print("\t {}".format(task.get("title")))
