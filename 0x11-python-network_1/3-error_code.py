#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    from urllib import error, request
    from sys import argv

    url = argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
