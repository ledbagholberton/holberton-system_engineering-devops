/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def count_words(subreddit, word_list)
    """Read reddit API and return top 10 hotspots """
    username = 'ledbag123'
    password = 'Reddit72'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    payload = {"limit": "150"}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False, params=payload)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        if (len(host_list) < len(list_titles) - 1):
            for word in word_list:
                counter = len([x for x in s.split() if x == word])
                (list_titles[len(host_list)]['data']['title'])
                recurse(subreddit, host_list)
        else:
            print(host_list)
            return()
    else:
        return(None)
