#!/usr/bin/python3
"""sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response """

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    # set variable to send in POST request
    values = {'email': email}

    # encode values to send
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    # Make POST request
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        header = response.read()
        print(header.decode('utf-8'))
