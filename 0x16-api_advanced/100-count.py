#!/usr/bin/python3
""" Used to count """
from requests import get


def count_words(subreddit, word_list, after="", word_dic={}):
    """
    a recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords (case-insensitive,
    delimited by spaces. Javascript should count as javascript,
    but java should not).
    """
    if not word_dic:
        for word in word_list:
            word_dic[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in word_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower(), w[1]))
        return None

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    req = get(url, headers={'user-agent': 'my-app/0.0.1'},
              params={'limit': 100, 'after': after}, allow_redirects=False)

    if req.status_code != 200:
        return None

    try:
        jsonf = req.json()

    except ValueError:
        return None

    try:

        data = jsonf.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower = [s.lower() for s in title.split(' ')]

            for w in word_list:
                word_dic[w] += lower.count(w.lower())

    except Exception:
        return None

    count_words(subreddit, word_list, after, word_dic)
