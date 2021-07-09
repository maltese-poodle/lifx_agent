#!/usr/bin/python
import os
import requests

def get_auth_header():
    return {"Authorization": "Bearer %s" % os.getenv('LIFX_API_KEY')}

def get_devices():
    return requests.get('https://api.lifx.com/v1/lights/all', headers=get_auth_header())

print(get_devices())
