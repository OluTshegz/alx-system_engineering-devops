#!/usr/bin/python3
"""Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords"""

import requests


def count_words(subreddit, word_list):
    """
    Prints a sorted count of given keywords (case-insensitive,
    delimited by spaces. Javascript should count as javascript,
    but java should not).
    If no posts match or the subreddit is invalid, print nothing.
    """
    if subreddit is None or not subreddit or not isinstance(subreddit, str):
        return

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': 'Google Chrome Version 125.0.6422.142'}
    query_params = {'limit': 100}
    try:
        response = requests.get(url, headers=user_agent, params=query_params, allow_redirects=False)

        if response.status_code != 200:
            return

        data = response.json().get('data')
        children = data.get('children')

        word_count = {}
        for child in children:
            title = child.get('data').get('title').lower()
            for word in word_list:
                if word.lower() in title:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_words:
            print('{}: {}'.format(word, count))
    except Exception:
        return