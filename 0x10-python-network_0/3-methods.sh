#!/bin/bash
#takes in a URL and displays all HTTP Methods The Server Will Accept.
curl -sI "$1" | grep "Allow" | cat -d " " -f2-
