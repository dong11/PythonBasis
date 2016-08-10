from urllib import request
import re


def get_html():
    with request.urlopen("http://tieba.baidu.com/index.html") as f:
        data = f.read().decode('gbk')  # html为gbk编码
        return data


def get_images():
    # restr = r'('
    # restr += r'http:\/\/[^\s,"]*\.jpg'
    # restr += r'|http:\/\/[^\s,"]*\.jpeg'
    # restr += r'|http:\/\/[^\s,"]*\.png'
    # restr += r'|http:\/\/[^\s,"]*\.gif'
    # restr += r'|http:\/\/[^\s,"]*\.bmp'
    # restr += r'|https:\/\/[^\s,"]*\.jpg'
    # restr += r'|https:\/\/[^\s,"]*\.jpeg'
    # restr += r'|https:\/\/[^\s,"]*\.png'
    # restr += r'|https:\/\/[^\s,"]*\.gif'
    # restr += r'|https:\/\/[^\s,"]*\.bmp'
    # restr += r')'

    restr = '<img.*?src="(.*?)"'

    imgre = re.compile('<img.*?src="(.*?)"')
    imglist = re.findall(imgre, get_html())
    for img in imglist:
        print(img)


print(get_html())

print('*********************************')

get_images()
