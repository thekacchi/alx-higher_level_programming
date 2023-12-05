#!/bin/bash
url=$1
url -sI "$url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r\n'
