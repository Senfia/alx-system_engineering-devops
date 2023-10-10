#!/usr/bin/python3
"""
Queries the Reddit API
parses the title of all hot articles, and prints
a sorted count of given keywords (case-insensitive,
delimited by spaces
"""

import requests
import sys


def count_words(subreddit, word_list=[], count_dict={}, after=""):
    """
    Queries the Reddit API
    """
    if subreddit is None or len(word_list) == 0:
        return None
    if len(count_dict) == 0:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=500&after={}".format(
            subreddit, after)
    req = requests.get(url, headers={'user-agent': 'Chrome'})
    if req.status_code is not 200:
        return None
    children = req.json()['data']['children']
    if count_dict == {}:
        for word in word_list:
            count_dict[word.lower()] = 0
    for child in children:
        temp = child['data']['title'].split(' ')
        for substring in temp:
            if substring.lower() in word_list:
                count_dict[substring.lower()] += 1

    current_after = req.json()['data']['after']

    if current_after is None:
        for count_item in sorted(count_dict.items(), key=lambda x: x[1],
                                 reverse=True):
            if int(count_item[1]) > 0:
                print("{}: {}".format(count_item[0], count_item[1]))
        return
    return count_words(subreddit, word_list, count_dict, current_after)
