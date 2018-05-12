#!/usr/bin/env python

from bs4 import BeautifulSoup
import time
import urllib.request
import os
import requests

def download_pic(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
    urllib.request.install_opener(opener)
    split_url = url.split('/')
    filename = split_url.pop()
    urllib.request.urlretrieve(url, filename='/home/SSKeng/Desktop/python/imgcl/'+filename)


def get_page(page_url):
    req = requests.get(page_url, headers=headers)
    content =  req.content
    f = open('log', 'w')
    print >>f, content
#    content = f.read()
    soup = BeautifulSoup(content, 'lxml')
    img_list =  soup.find_all('input', attrs={"type":"image"})
    for img in img_list:
        img_url = img['src']
        download_pic(img_url)

def main(base_url):
    for page in range(1,2):
        page_url = BASE_PAGE_URL+str(page)
        req = requests.get(page_url, headers=headers)
        

if __name__ == '__main__':
    BASE_PAGE_URL = ''
    headers = {
    'Host':'www.jnpxba.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36' } 
    main(BASE_PAGE_URL)

#--------- input label--------------
#    img_list =  soup.find_all('input', attrs={'type':'image'})
#    for img in img_list:
#        img_url = 
#        print img
#        print '-'*30
