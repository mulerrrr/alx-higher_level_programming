#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) == 2:
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}
    # Send post request
    response = requests.post('http://0.0.0.0:5000/search_user', data=values)
    if response.headers.get('content-type') == 'application/json':
        if not response.json():
            print("No result")
        else:
            print("[{}] {}\
".format(response.json()['id'], response.json()['name']))
    else:
        print("Not a valid JSON")
