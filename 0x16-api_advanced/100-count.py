#!/usr/bin/python3
""" The following script is for counting Reddit API word
"""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """
    This method counts the occurrences of words in the titles of hot articles
    from a given subreddit

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to count.
        after (str, optional): The Reddit API parameter for pagination.
        count (list, optional): A list to store the counts of each word.

    Returns:
        int : the number of occurences of a word
        or None
    """

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'api_advanced_project'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for x in range(len(word_list)):
                    if word_list[x].lower() == word.lower():
                        count[x] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for a in range(len(word_list)):
                for b in range(a + 1, len(word_list)):
                    if word_list[a].lower() == word_list[b].lower():
                        save.append(b)
                        count[a] += count[b]

            for a in range(len(word_list)):
                for b in range(a, len(word_list)):
                    if (count[b] > count[a] or
                            (word_list[a] > word_list[b] and
                             count[b] == count[a])):
                        var = count[a]
                        count[a] = count[b]
                        count[b] = var
                        var = word_list[a]
                        word_list[a] = word_list[b]
                        word_list[b] = var

            for a in range(len(word_list)):
                if (count[a] > 0) and a not in save:
                    print("{}: {}".format(word_list[a].lower(), count[a]))
        else:
            count_words(subreddit, word_list, after, count)
