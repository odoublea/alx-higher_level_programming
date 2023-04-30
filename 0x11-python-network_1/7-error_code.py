#!/usr/bin/python3
"""Write a Python script that tak"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
