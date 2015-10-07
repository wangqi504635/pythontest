__author__ = 'wangqi'
# -*- coding:utf-8 -*-
import urllib.request
import re
from bs4 import BeautifulSoup




def getHtml(url):
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    response = opener.open(url)
    html = response.read()
    html = html.decode('utf-8')
    return html

# url = "http://www.juzimi.com/"
url = "http://www.juzimi.com/ju/55412"
substr = "http://www.juzimi.com/ju/"

html = getHtml(url)
content_re = ".*句子欣赏评论: “(.*)” 原作者：.*"
author_re = ".*原作者：(.*)出处：出自.*"
book_re = ".*出处：出自《(.*)》.*"

result = re.findall(content_re,html)
for juzi in result:
    print(juzi)

result = re.findall(author_re,html)
for juzi in result:
    print(juzi)

result = re.findall(book_re,html)
for juzi in result:
    print(juzi)


soup = BeautifulSoup(html,"lxml")

for meta in soup.find_all('meta'):
    if meta.has_attr('name') and meta.attrs['name'] == 'description':
        content = meta.attrs['content']
        print(content)


