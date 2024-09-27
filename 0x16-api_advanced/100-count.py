#!/usr/bin/python3
"""
Module Name: 100-count
Description: This module contains a recursive function to query the
             Reddit API and count occurrences of given keywords in
             the titles of hot articles in a given subreddit.
"""

import requests
from collections import defaultdict
import re


def count_words(subreddit, word_list, word_count=None, after=None):
    """Recursively fetches titles from a subreddit and counts the
    occurrences of specified words.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of words to count.
        word_count (dict): A dictionary to store word counts (default None).
        after (str): Pagination parameter (default None).

    Returns:
        None: Prints results directly.
    """
    if word_count is None:
        word_count = defaultdict(int)

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my_reddit_api/0.1'}  # Descriptive User-Agent
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        if 'children' in data and data['children']:
            for post in data['children']:
                title = post['data']['title']
                # Normalize the title for counting
                title_words = re.findall(r'\b\w+\b', title.lower())  # Find all words
                for word in word_list:
                    # Count occurrences of each word
                    word_count[word] += title_words.count(word.lower())

            after = data.get('after')
            if after:
                return count_words(subreddit, word_list, word_count, after)  # Recursive call
        else:
            print("")  # No valid posts
            return
    else:
        print("")  # Invalid subreddit or no posts
        return

    # Sorting results by count (descending) and alphabetically
    sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    # Printing the counts
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")


# Main testing block for debugging
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
