__author__ = 'wangqi'
# -*- coding:utf-8 -*-

from html.parser import HTMLParser

from model.juzi import juzi


class JZMParser(HTMLParser):

    a_text = False
    juzi = juzi()

    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.content = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.a_text = True
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == 'href':
                        self.links.append(value)

    def handle_endtag(self, tag):
        if tag == 'a':
            self.a_text = False

    def handle_data(self, data):
        if self.a_text:
            self.content.append(data)
