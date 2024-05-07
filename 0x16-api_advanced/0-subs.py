#!/usr/bin/python3
"""Used to return the number of subscribers available."""
from requests import get


def number_of_subscribers(subreddit):
    """ returns the length of subredits subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'user-agent': 'my-app/0.0.1'}

    req = get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return 0

    try:
        jsonf = req.json()
    except ValueError:
        return 0

    data = jsonf.get("data")

    if data:
        sub_count = data["subscribers"]
        if sub_count:
            return sub_count

    return 0
