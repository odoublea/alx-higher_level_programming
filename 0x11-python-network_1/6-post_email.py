#!/usr/bin/python3
"""  Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally displays
the body of the response."""


if __name__ == "__main__":
    import requests
    from sys import argv

    url, email = argv[1:]

    req = requests.post(url, {"email": email})
    print(req.text)
