#!/usr/bin/python3

import requests as req

resp = req.get("http://www.something.com")

print(resp.text)
