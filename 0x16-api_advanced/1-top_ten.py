#!/usr/bin/python3
"""
The following script prints the titles of the first 10 hot posts
listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    THis method prints the titles of the 1st 10 hot posts
    listed for a subreddit

    Args:
        subreddit (str): The name of the subreddit
                        for which to retrieve hot posts

    Returns:
        - The titles of the first 10 hot posts for the specified subreddit.
        - None (if the subreddit is invalid or an error occurs
        during the API request)
    """

    # Checking if the subreddit is valid
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    # Defining user agent for the Reddit API request
    headers = {'User-agent': 'Google Chrome Version 91.0.4472.124'}

    # Setting params for the API request (limiting to the first 10 posts)
    params = {'limit': 10}

    # Creating the URL for the Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    # Sending a GET request to Reddit API
    # With the specified user agent and params
    response = get(url, headers=headers, params=params)

    # Parsing the JSON response from the Reddit API
    results = response.json()

    try:
        # Extracting the list of posts from the API response
        posts = results.get('data').get('children')

        # Printing the titles of the first 10 posts
        for post in posts:
            print(post.get('data').get('title'))

    except Exception as e:
        # Handling exceptions and printing an error message
        print("None")
