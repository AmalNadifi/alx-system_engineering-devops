#!/usr/bin/python3
""" The following script is for counting Reddit API word
"""

import requests


def count_words(subreddit, word_list, after="", counter=[]):
    """
    This method counts the occurrences of words in the titles of hot articles
    from a given subreddit

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to count.
        after (str, optional): The Reddit API parameter for pagination.
        count (list, optional): A list to store the counts of each word.

    Returns:
        None
    """

    # Initialize counter if not provided
    if after == "":
        counter = [0] * len(word_list)

    # API request to get hot articles
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'user-agent': 'api_advanced-project'}
    params = {'after': after}
    response = requests.get(
            url, params=params, allow_redirects=False, headers=headers)

    # Check if the API request was successful
    if response.status_code == 200:
        data = response.json()

        # Iterate through each hot article
        for topic in data['data']['children']:
            # Iterate through each word in the title
            for word in topic['data']['title'].split():
                # Check if the word is in the word_list
                for x in range(len(word_list)):
                    if word_list[x].lower() == word.lower():
                        counter[x] += 1

        # Get the 'after' parameter for pagination
        after = data['data']['after']

        # If 'after' is None, print the results
        if after is None:
            saving = []
            for x in range(len(word_list)):
                for y in range(x + 1, len(word_list)):
                    if word_list[x].lower() == word_list[y].lower():
                        saving.append(y)
                        counter[x] += counter[y]
            for x in range(len(word_list)):
                for y in range(x, len(word_list)):
                    if (counter[y] > counter[x] or
                            (word_list[x] > word_list[y] and
                                counter[j] == counter[i])):
                        var = counter[i]
                        counter[i] = counter[j]
                        counter[j] = var
                        var = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = var

            for i in range(len(word_list)):
                if (counter[i] > 0) and i not in saving:
                    print("{}: {}".format(word_list[i].lower(), counter[i]))
        else:
            # If 'after' is not None, make a recursive call
            count_words(subreddit, word_list, after, counter)
