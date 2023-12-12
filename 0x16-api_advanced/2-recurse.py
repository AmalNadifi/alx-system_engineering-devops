#!/usr/bin/python3
""" The following script defines a recursive function that queries
the Reddit API and returns a list containing the titles of all hot articles
for a given subreddit
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    This method recursively queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit
    Args:
        subreddit (str): The name of the subreddit
        hot_list (list, optional): A list to store the titles of hot articles

    Returns:
        list or None: A list containing the titles of all hot articles for the
        given subreddit. Returns None if no results are found or if
        the subreddit is invalid
    """
    global after

    # Base case: If subreddit is not valid, return None
    if subreddit is None or not isinstance(subreddit, str):
        return None

    # Defining user agent for the Reddit API request
    headers = {'User-agent': 'Google Chrome Version 91.0.4472.124'}

    # Setting parameters for the API request
    params = {'limit': 100, 'after': after}

    # Creating the URL for the Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    # Sending a GET request to the Reddit API with user agent and parameters
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Parsing the JSON response from the Reddit API
    results = response.json()

    try:
        # Extracting the list of posts from the API response
        posts = results.get('data').get('children')

        # Appending the titles of the current set of posts to the hot_list
        for post in posts:
            hot_list.append(post.get('data').get('title'))

        # Recursively calling the func with the 'after' param for pagination
        if results.get('data').get('after') is not None:
            hot_list = recurse(
                subreddit, hot_list, after=results.get('data').get('after')
            )
        return hot_list

    except Exception as e:
        # Handle exceptions and print an error message
        return (None)
