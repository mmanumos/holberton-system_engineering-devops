#!/usr/bin/python3
""" Function to return a value getted by an API """
import requests as re


def top_ten(subreddit):
    """ Return number of subscribers """
    headers = {'User-agent': 'me'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    data = re.get(url, headers=headers, allow_redirects=False).json()
    try:
        my_list = data.get('data').get('children')
        for value in my_list[0:10]:
            print(value.get('data').get('title'))
    except:
        print(None)
