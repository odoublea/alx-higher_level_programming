#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request

    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        the_page = response.text
        print("Body response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
