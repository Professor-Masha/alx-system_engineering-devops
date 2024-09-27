# Reddit API Project

This project consists of Python scripts that interact with the Reddit API to retrieve and analyze hot articles from specific subreddits. The functionality includes counting keyword occurrences in article titles using recursive API calls.

## Features

- Query the Reddit API to retrieve hot articles from a specified subreddit.
- Count occurrences of given keywords in the article titles.
- Handle pagination to ensure all articles are considered.
- Print results sorted by count in descending order and alphabetically for ties.

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests

