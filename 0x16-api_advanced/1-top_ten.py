#!/usr/bin/python3
"""Function to query the top ten posts of a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the top ten hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("OK")  # Indicate subreddit does not exist
        return

    if response.status_code != 200:
        print("OK")  # Indicate some other error
        return

    try:
        r = response.json()
        posts = r.get("data").get("children", [])
        for post in posts[:10]:
            print(post["data"]["title"])
    except ValueError:
        print("OK")  # Indicate JSON decoding error


# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
    else:
        top_ten(sys.argv[1])
