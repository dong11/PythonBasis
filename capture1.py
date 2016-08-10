# 爬取糗事百科的小段子
from urllib import request
import re

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

req = request.Request('http://www.qiushibaike.com/hot/page/1', None, headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')

pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class' +
                     '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
items = re.findall(pattern, html)

print(html)

print('**********************************')
print('**********************************')
print('**********************************')

for item in items:
    print(item[0], item[1], item[2], item[3], item[4])

print('**********************************')
print('**********************************')

for item in items:
    haveImg = re.search('img', item[3])
    if not haveImg:
        print(item[0], item[1], item[2], item[4])
