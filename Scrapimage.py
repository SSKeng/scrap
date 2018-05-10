#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import time
import urllib
import os

def download_pic(url):
    split_url = url.split('/')
    filename = split_url.pop()
    urllib.urlretrieve(url, filename='/home/ss/Desktop/python/img/'+filename)


def get_page(page_url):
#    req = requests.get(page_url, headers=headers)
#    content =  req.content
    f = open('log', 'r')
#    print >>f, content
    content = f.read()
    soup = BeautifulSoup(content, 'lxml')
    img_list =  soup.find_all('img', attrs={"class":"img-responsive lazy image_dta"})
    for img in img_list:
        img_url = img['data-original']
        download_pic(img_url)

def main():
    for page in range(1,2):
        url = BASE_PAGE_URL+str(page)
        print url
        get_page(url)

if __name__ == '__main__':
#    BASE_PAGE_URL = 'http://www.jnpxba.com/thread0806.php?fid=16&search=&page='
    headers = {
    'Host':'www.doutula.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36' } 
    BASE_PAGE_URL = 'http://www.doutula.com/photo/list/?page='
    main()

#--------- input label--------------
#    img_list =  soup.find_all('input', attrs={'type':'image'})
#    for img in img_list:
#        img_url = 
#        print img
#        print '-'*30
