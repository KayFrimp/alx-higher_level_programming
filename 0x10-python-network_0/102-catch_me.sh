#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!"
curl -s -X POST http://0.0.0.0:5000/catch_me -d "You got me!"
