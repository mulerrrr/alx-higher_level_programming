#!/bin/bash
# Get content length of a url
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
