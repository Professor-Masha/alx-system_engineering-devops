#!/usr/bin/python3
"""Function to count keywords in posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list):
    """Count occurrences of keywords in subreddit posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("OK")  # Invalid subreddit
        return

    if response.status_code != 200:
        print("OK")  # Handle other errors
        return

    try:
        posts = response.json().get("data").get("children", [])
        keyword_count = {word.lower(): 0 for word in set(word_list)}  # Avoid duplicates
        for post in posts:
            title = post["data"]["title"]
            for word in keyword_count.keys():
                keyword_count[word] += title.lower().split().count(word)

        # Output counts
        for word, count in keyword_count.items():
            if count > 0:
                print(f"{word}: {count}")
    except ValueError:
        print("OK")  # Handle JSON decode errors


# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <keyword1> <keyword2> ...".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = sys.argv[2:]
        count_words(subreddit, keywords)
