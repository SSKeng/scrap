#!/usr/bin/env/ python3
# _*_ coding: utf-8 _*_

import re

def find_chinese():
    find_count = 0
    with open('Chinese.txt', 'wb') as outfile:
        with open('Localizable.strings', 'rb') as infile:
            while True:
                content = infile.readline()
                if re.match(ur'''.*?[\u4E00-\u9FA5]+''', content.decode('utf-8')):
                    #print content
                    outfile.write(content)
                    find_count += 1
                

                if not content:
                    return find_count
            outfile.close()
            infile.close()
    

def delete_str():
    count = 0
    with open('Chinese.txt', 'rb') as infile:
        with open('Fina.txt', 'wb') as outfile:
            while True:
                content = infile.readline()
                
                if content.startswith('//') or content.startswith(' '):
                    pass
                else:
                    outfile.write(content)
                    count +=1
                if not content:
                    return count
                
if __name__ == '__main__':
    count = find_chinese()
    print('查找结束！ count =', count)
    c = delete_str()
    print('count = ',c)

