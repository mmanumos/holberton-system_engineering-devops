#!/usr/bin/python3
import requests as re


def number_of_subscribers(subreddit):
    """ Return number of subscribers """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'me'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = re.get(url, headers=headers).json()
    print(data.get('data'))
    try:
        return (data.get('data').get('subscribers'))
    except:
        return 0
