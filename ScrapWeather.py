#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

headers = {
'Host':'www.weather.com.cn',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

req = requests.get('http://www.weather.com.cn/textFC/hb.shtml', headers = headers)
f = open('log', 'w')
print >>f, req.content
