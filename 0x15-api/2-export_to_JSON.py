#!/usr/bin/python3
""" This module using the given REST API, for a given employee ID,
exports data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_ot = res.json()
    name = json_ot.get('username')

    todos = '{}todos?userid={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()
    t_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        t_task.append(dict_task)

    d_task = {str(userid): t_task}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
