#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    username = argv[1]
    passwd = argv[2]

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, passwd)

    response = requests.get(url, auth=auth)
    data = response.json()
    print(data.get('id'))
