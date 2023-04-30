#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    import requests
    from sys import argv

    q = argv[1] if len(argv) > 1 else ''

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
