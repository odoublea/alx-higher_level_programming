#!/usr/bin/python3
"""Write a Python script that tak"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]

    try:
        print(requests.get(url))
    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(e.code))
