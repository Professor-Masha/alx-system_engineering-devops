#!/usr/bin/python3
"""
Module Name: 0-subs
Description: This module contains a function to query the Reddit API
             for the number of subscribers in a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Fetches the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers or 0 if subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    return 0
