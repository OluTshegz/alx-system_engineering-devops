#!/usr/bin/python3
"""Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list containing the titles of
    all hot articles for a given subreddit.
    If not a valid subreddit, return None.
    """
    if subreddit is None or not subreddit or not isinstance(subreddit, str):
        return None

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': 'Google Chrome Version 125.0.6422.142'}
    query_params = {'after': after, 'count': count}
    try:
        response = requests.get(url, headers=user_agent,
                                params=query_params, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get('data')
        after = data.get('after')
        count += data.get('dist')
        children = data.get('children')

        for child in children:
            hot_list.append(child.get('data').get('title'))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list

    except Exception:
        return None
