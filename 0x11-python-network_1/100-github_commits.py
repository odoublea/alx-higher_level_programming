#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge."""


if __name__ == "__main__":
    import requests
    from sys import argv

    owner = argv[1]
    repo = argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        try:
            for i in range(10):
                print("{}: {}".format(data[i].get('sha'), data[i].get(
                    'commit').get('author').get('name')))
        except IndexError:
            pass

    else:
        print("Error: Could not retrieve data for repository {}. \
            Status code: {}".format(repo, response.status_code))
