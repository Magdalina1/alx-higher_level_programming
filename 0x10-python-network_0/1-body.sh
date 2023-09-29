#!/bin/bash
# Take in a URL, Sends a GET request to the URL, Displays the body of the of the response
curl -sX GET "$1" -L 200
