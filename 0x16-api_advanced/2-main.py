#!/usr/bin/python3
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        host_list=[]
        result = recurse(sys.argv[1], host_list)
        if result is not None:
            print(len(result))
        else:
            print("None")
