#!/bin/bash
# Takes in a URL, sends a request and displays body response size
curl -s "$1" | wc -c
