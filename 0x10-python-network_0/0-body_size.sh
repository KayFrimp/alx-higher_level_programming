#!/bin/bash
# Takes in a URL, sends a request and displays body response size
curl -s "$url" | wc -c
