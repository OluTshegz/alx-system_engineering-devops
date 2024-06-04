#!/usr/bin/python3
"""Queries the Reddit API and returns the
    number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    if subreddit is None or not subreddit or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'Google Chrome Version 125.0.6422.142'}
    try:
        response = requests.get(url, headers=user_agent)
        if response.status_code == 200:
            response_json = response.json()
            for key, value in response_json.items():
                if key == 'data':
                    for data_key, data_value in value.items():
                        if data_key == 'subscribers':
                            return data_value
                        else:
                            return 0
                else:
                    return 0
        else:
            return 0
    except Exception:
        return 0
