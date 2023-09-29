#!/bin/bash
# Takes in URL, sends a Request to that URL, displays the size of the body of the response.
curl -sI GET "$1" | grep -i "content-length" | cat -d " " -f2
