#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge."""


if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = requests.get(url)
    data = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(data[i].get('sha'), data[i].get(
                'commit').get('author').get('name')))
    except IndexError:
        pass
