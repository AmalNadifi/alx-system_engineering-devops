#!/usr/bin/python3
""" The following module returns the number of subscribers
for a given subreddit
"""


from requests import get


def number_of_subscribers(subreddit):
    """
    THis function queries the REDDIT API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit

    Args:
        subreddit (str): The name of the subreddit for which
        the subscriber count is requested

    Returns:
        int : The total number of subscribers for the subreddit
        0 : if the subreddit is not valid
            or if an exception occurs during the request
    """
    # Checking if the provided subreddit is valid
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Defining a user agent for the Reddit API request
    user_agent = {'User-agent': 'Google Chrome Version 91.0.4472.124'}

    # Creating the URL for the Reddit API request
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # Sending a GET request to the Reddit API with the specified user agent
    response = get(url, headers=user_agent)

    # Parsing the JSON response from the Reddit API
    results = response.json()

    try:
        # Extracting the number of subscribers from the API response
        return results.get('data').get('subscribers')

    except Exception:
        # Handling exceptions and returning 0 if an error occurs
        return 0
