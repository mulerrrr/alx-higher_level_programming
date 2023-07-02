#!/bin/bash
# Get status code
curl -s "$1" -o /dev/null -w '%{http_code}'
