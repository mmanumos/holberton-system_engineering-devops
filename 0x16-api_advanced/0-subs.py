#!/usr/bin/python3
""" Function to return a value getted by an API """
import requests as re


def number_of_subscribers(subreddit):
    """ Return number of subscribers """
    headers = {'User-agent': 'me'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = re.get(url, headers=headers, allow_redirects=False).json()
    try:
        return (data.get('data').get('subscribers'))
    except:
        return 0
