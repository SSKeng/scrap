#!/usr/bin

import requests
from bs4 import BeautifulSoup

url = 'https://baike.baidu.com/item/%E5%9B%BD%E6%9C%89%E4%BC%81%E4%B8%9A/3457818?fr=aladdin'
headers = {'Host':'baike.baidu.com',
'Referer':'https://www.baidu.com/link?url=tatE6ZlIl97ClYjaLBrNnHsHGBH3kzgWrBARv8ZW2lDYT4TixjcqFByFQDsZo5cEfG8eKP91Z3oqYN7tosofhm8CTnZBZR8pHq3bAA8qOJaTi2OXJH_Shh6XJ8Q4QQup&wd=&eqid=cd7cdfcd00000085000000065afa59d3',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
#req = requests.get(url, headers = headers)
#content = req.content

f = open('log', 'rb')
#f.write(content)
content = f.read()

soup = BeautifulSoup(content, 'lxml')
table_list = soup.find_all('table', class_ = 'table-view log-set-param')

for index, table in enumerate(table_list):
    if index==0:
        print ("国务院直属企业")
        print ("-"*30)
    else:
        print ("\n")
        print ("中央企业")
        print ("-"*30)
    tr_list = table.find_all('tr')[1:]
    for tr in tr_list:
        td_list = tr.find_all('td')
        print ('%s:%s'%(td_list[0].text, td_list[1].text))

