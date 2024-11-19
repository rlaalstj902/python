import os
import sys
import urllib.request
import datetime
import time
import json

client_id = 'IV6k7lOUikupnX7LZlt4'
client_secret = 'FI0LGxdKO_'

#[CODE1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-id", client_id)
    req.add_header("X-Naver-Client-Secret",client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() ==200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf')
