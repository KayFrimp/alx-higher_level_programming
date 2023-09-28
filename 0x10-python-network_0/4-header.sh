#!/bin/bash
# Bash script displays all HTTP methods the server will accept using curl
curl -s -H "X-School-User-Id: 98" "$1"
