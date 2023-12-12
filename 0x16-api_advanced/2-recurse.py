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

    # Base case: If subreddit is not valid, return None
    if subreddit is None or not isinstance(subreddit, str):
        return None

    # Defining user agent for the Reddit API request
    headers = {'User-agent': 'api_advanced-project'}

    # Setting parameters for the API request
    parameters = {'after': after}

    # Creating the URL for the Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    # Sending a GET request to the Reddit API with user agent and parameters
    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)

    if response.status_code == 200:
        # Extract 'after' data from the API response
        after_data = response.json().get("data").get("after")
        # If 'after' data is present, make a recursive call to fetch more posts
        if after_data is not None:
            recurse(subreddit, hot_list)
        # Extract posts from the current set of posts and append to hot_list
        all_posts = response.json().get("data").get("children")
        for post in all_posts:
            hot_list.append(post.get("data").get("title"))
        return hot_list
    else:
        # Return None if there's an issue with the API request
        return None
