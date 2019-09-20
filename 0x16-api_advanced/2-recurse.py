#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def recurse(subreddit, host_list=[]):
    """Read reddit API and return top 10 hotspots """
    username = 'ledbag123'
    password = 'Reddit72'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    try:
        list_titles = r.json()['data']['children']
        print("list_titles len:", len(list_titles))
        print("host_list len:", len(host_list))
        if (len(host_list) <= len(list_titles)):
            print(list_titles[20]['data']['title'])
            host_list.append(list_titles[len(host_list + 1)]['data']['title'])
            print(host_list)
            recurse(subreddit, host_list)
        else:
            return(host_list)
    except:
        return("None")
