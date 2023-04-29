#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request to the 
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)."""


if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv

    url, email = argv[1:]

    data = parse.urlencode({"email": email})
    data = data.encode("ascii")
    req = request.Request(url, email)

    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
