import urllib.request
import os
import re


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    response = urllib.request.urlopen(req)
    html = response.read().decode()
    
    return html


def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p, html)
    
    for each in imglist:
        fileName = each.split('/')[-1]
        urllib.request.urlretrieve(each,fileName)


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/3563409202'
    get_img(url_open(url))
