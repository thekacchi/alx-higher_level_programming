#!/bin/bash
# Usage: ./script_name.sh <URL>
curl -s -w "%{http_code}" "$1" | awk '/^200$/ {flag=1; next} flag {print}'
