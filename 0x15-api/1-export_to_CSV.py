#!/usr/bin/python3
""" Exporting csv files"""
import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        my_id = sys.argv[1]
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(my_id)
        dict1 = requests.get(url).json()
        username = dict1.get('username')
        url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.\
               format(my_id)
        list2 = requests.get(url2).json()
        dict_tasks = {}
        t_total = 0
        with open('USER_ID.csv', mode='w') as csv_file:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                          'TASK_TITLE']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                    quotechar='"')
            writer.writeheader()
            for tasks in list2:
                if tasks.get('userId') == int(my_id):
                    status = tasks.get('completed')
                    text = tasks.get('title')
                    writer.writerow({'USER_ID': my_id, 'USERNAME': username,
                                     'TASK_COMPLETED_STATUS': status,
                                     'TASK_TITLE': text})
