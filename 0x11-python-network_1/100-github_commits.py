#!/usr/bin/python3

if __name__ == "__main__":
    import requests
    from sys import argv

    owner, repo = argv[1:]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    data = response.json()
    for i in data:
        print(i)
    #if data:
     #   print("{}: {}".format(data['<sha>'], data['<author name>']))
