#!/usr/bin/python3
"""
Module Name: 2-recurse
Description: This module contains a recursive function to query the
             Reddit API for all hot article titles in a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively fetches the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store hot article titles (default None).
        after (str): The parameter for pagination (default None).

    Returns:
        list: A list of hot article titles or None if invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        if 'children' in data:
            hot_list.extend([post['data']['title'] for post in data['children']])
            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list, after)  # Recursive call
            return hot_list
    return None
