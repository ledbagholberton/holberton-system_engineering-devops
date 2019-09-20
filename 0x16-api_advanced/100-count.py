#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def count_words(subreddit, word_list, after="null", host_list=[]):
    """Read reddit API and return top 10 hotspots """
    username = 'ledbag123'
    password = 'Reddit72'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    payload = {"limit": "100", "after": after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False, params=payload)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        after = r.json()['data']['after']
        if after is not None:
            try:
                host_list.append(list_titles[len(host_list)]['data']['title'])
            except:
                pass
            count_words(subreddit, word_list, after, host_list)
        else:
            my_count = [0] * len(word_list)
            for title in host_list:
                for pos in range(len(word_list)):
                    counter = len([x for x in title.split()
                                   if x == word_list[pos]])
                    my_count[pos] += counter
            for pos in range(len(word_list)):
                print("{}: {}".format(word_list[pos], my_count[pos]))
    else:
        return(None)
