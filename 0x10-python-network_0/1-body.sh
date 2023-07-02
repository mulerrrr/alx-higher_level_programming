#!/bin/bash
# Get url when code in status line is 200 ok - current situation is a redirection so we use flag -L
curl -s -L -X GET "$1"
