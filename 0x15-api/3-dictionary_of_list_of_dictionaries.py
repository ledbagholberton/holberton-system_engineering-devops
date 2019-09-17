#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


if __name__ == "__main__":
    user_list = []
    name_list = []
    url = 'https://jsonplaceholder.typicode.com/users/'
    dict1 = requests.get(url).json()
    for users in dict1:
        user_list.append(users.get('id'))
        name_list.append(users.get('username'))
    dict_tasks = {}
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    list2 = requests.get(url2).json()
    for my_id in user_list:
        username = name_list[my_id - 1]
        dict_tasks[my_id] = []
        for users in list2:
            if my_id == users.get('userId'):
                status = users.get('completed')
                text = users.get('title')
                dict_tasks[my_id].append({"task": text, "completed":
                                          status, "username": username})
    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(dict_tasks, outfile)
