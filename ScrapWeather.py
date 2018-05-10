#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import time
import json
from echarts import Echart, Bar, Axis

def city_temp(url_a):
    headers = {
    'Host':'www.weather.com.cn',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

    req = requests.get(url_a, headers = headers)
    content = req.content

    soup = BeautifulSoup(content, 'lxml')
    conMidtab = soup.find('div', class_ = 'conMidtab')
    conModtab2_list = conMidtab.find_all('div', class_ = 'conMidtab2')
    for conModtab2 in conModtab2_list:
        tr_list =  conModtab2.find_all('tr')[2:]
        for index, tr in enumerate(tr_list):
            if index == 0:
                td_list =  tr.find_all('td')
                province = td_list[0].text.replace('\n', '')
                city = td_list[1].text.replace('\n', '')
                max_tem = td_list[4].text   
            else:
                td_list = tr.find_all('td')
                city = td_list[0].text.replace('\n', '')
                max_tem = td_list[3].text
            city_tem_list.append({'city':province+city, 'tem':max_tem})

if __name__ == "__main__":
    city_tem_list = []
#    url = 'http://www.weather.com.cn/textFC/'
#    area_list = ['hb.shtml', 'db.shtml', 'hd.shtml', 'hz.shtml', 'hn.shtml', 'xb.shtml', 'xn.shtml']
#    for area in area_list:
#        city_temp(url+area)
#        time.sleep(20)

#    line = json.dumps(city_tem_list, ensure_ascii=False)
#    with open('tem.json', 'w') as fp:
#        fp.write(line.encode('utf-8'))
    
       
    with open('tem.json', 'r') as fp:
        city_tem_list = json.load(fp, encoding='utf-8')

    sort_max_list = sorted(city_tem_list, lambda x,y: cmp(int(x['tem']), int(y['tem'])), reverse=True)
    top10_sort_list = sort_max_list[0:10]
    top10_tem_list = []
    top10_city_list = []
    for top10_sort in top10_sort_list:
        top10_city_list.append(top10_sort['city'])
        top10_tem_list.append(top10_sort['tem'])
            

    echart = Echart('the order of high tem', 'SSKeng study')
    bar = Bar('the highest tem', top10_tem_list)
    axis = Axis('category', 'bottom', data=top10_city_list)
    echart.use(bar)
    echart.use(axis)
    echart.plot()
    
    
    
