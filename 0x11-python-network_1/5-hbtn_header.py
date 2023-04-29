#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header."""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    response = requests.get(url)
    header = response.headers["X-Request-Id"]
    print(header)
