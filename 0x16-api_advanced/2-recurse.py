#!/usr/bin/python3
""" Function to return a value getted by an API """
import requests as re


def recurse(subreddit, hot_list=[], after=""):
    """ Return all titles in a list """
    headers = {'User-agent': 'me'}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    print(url)
    data = re.get(url, headers=headers, allow_redirects=False).json()
    try:
        list_children = data.get('data').get('children')
        for value in list_children:
            hot_list.append(value.get('data').get('title'))
    except:
        return None

    after = data.get('data').get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
