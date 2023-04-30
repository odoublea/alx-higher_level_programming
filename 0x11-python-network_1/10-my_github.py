#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import requests
    from sys import argv

    username, password = argv[1:]
    url = f"https://api.github.com/user"

    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        data = response.json()
        print(data.get('id'))
    else:
        print(None)
