#!/usr/bin/python3
"""
Module Name: 1-top_ten
Description: This module contains a function to query the Reddit API
             for the titles of the top ten hot posts in a given subreddit.
"""

import requests

def top_ten(subreddit):
    """Fetches the titles of the top ten hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles of the top ten posts or None if invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts[:10]:  # Get the first 10 posts
            print(post['data']['title'])
    else:
        print(None)
