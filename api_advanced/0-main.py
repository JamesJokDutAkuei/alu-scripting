#!/usr/bin/python3
"""
0-main
"""
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        number_of_subscribers(sys.argv[1])
        print("OK")
