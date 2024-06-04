#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    if subreddit is None or not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': 'Google Chrome Version 125.0.6422.142'}
    query_params = {'limit': 10}
    try:
        response = requests.get(url, headers=user_agent, params=query_params,
                                allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data')
        children = data.get('children')

        for child in children:
            print(child.get('data').get('title'))
    except Exception:
        print(None)
        return
