#!/bin/bash
# Send POST request specifying content type json and giving a json file as data to send to the respective path
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
