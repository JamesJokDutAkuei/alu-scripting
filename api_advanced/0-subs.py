#!/usr/bin/python3
"""DOC"""
import requests

def number_of_subscribers(subreddit):
    """Define the base URL for the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    """Define the custom User-Agent to avoid "Too Many Requests" error"""
    headers = {'User-Agent': 'reddit-subscriber-counter/0.1'}
    
    try:
        """Make a GET request to the Reddit API"""
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        """Check if the response status code is 200 (OK)"""
        if response.status_code == 200:
            """Parse the JSON response"""
            data = response.json()
            """Return the number of subscribers"""
            return data['data']['subscribers']
        else:
            """If the status code is not 200, return 0"""
            return 0
    except Exception:
        """If there is any exception (like network issues), return 0"""
        return 0

"""Test cases"""
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
