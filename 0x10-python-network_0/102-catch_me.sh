#!/bin/bash
#Write a script yo dolicit "You hot me!"
#curl -s -X POST http://0.0.0.0:5000/catch_me -d "You got me!" >/dev/null
curl -sLX PUT "0.0.0.0:5000/catch_me" -d "user_id=98" -H "Origin: HolbertonSchool"
