#!/bin/bash
#Write a script yo dolicit "You hot me!"
curl -s -X POST http://0.0.0.0:5000/catch_me -d "You got me!" >/dev/null
