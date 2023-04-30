#!/usr/bin/python3

if __name__ == "__main__":
    import requests
    from sys import argv

    owner, repo = argv[1:]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    data = response.json()
    my_data = data[:10]

    for i in my_data:
        print("{}: {}".format(i['sha'], i['commit']['author']['name']))
