__author__ = 'wangqi'
# -*- coding:utf-8 -*-
import urllib.request

from parser.JZMHtmlParser import JZMParser


def getHtml(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode('utf-8')
    return html

url = "http://www.juzimi.com/"

parser = JZMParser()
parser.feed(getHtml(url))
parser.close()

print(len(parser.links))
print(len(parser.content))


