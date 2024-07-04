#!/usr/bin/python3
"""DOCS"""
import requests


def top_ten(subreddit):
    """DOCS"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        if not children:
            print(None)
        for post in children[:10]:
            print(post['data']['title'])
    else:
        print(None)
