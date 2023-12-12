#!/usr/bin/python3
""" The following script is for counting Reddit API word
"""
import json
import requests


def count_words(subreddit, word_list, n_after='', d_words={}):
    """
    This method counts the occurrences of words in the titles of hot articles
    from a given subreddit

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to count.
        n_after (str, optional): The Reddit API parameter for pagination.
        d_words (list, optional): A list to store the counts of each word.

    Returns:
        int : the number of occurences of a word
        or None
    """

    word_list = map(lambda x: x.lower(), word_list)
    word_list = list(word_list)

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers={'User-Agent': 'Api_advanced_poriject'},
                            params={'after': n_after},
                            allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        result = response.json().get('data', None)

        if result is None:
            return
    except ValueError:
        return

    children = result.get('children', [])

    for post in children:
        title = post.get('data', {}).get('title', '')
        for keyword in word_list:
            for word in title.lower().split():
                if keyword == word:
                    d_words[keyword] = d_words.get(keyword, 0) + 1

    n_after = result.get('after', None)

    if n_after is None:
        sorted_dict = sorted(d_words.items(), key=lambda x: x[1],
                             reverse=True)

        for a in sorted_dict:
            if a[1] != 0:
                print("{}: {}".format(a[0], a[1]))
        return

    return count_words(subreddit, word_list, n_after, d_words)
