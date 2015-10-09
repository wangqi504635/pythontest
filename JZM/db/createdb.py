__author__ = 'wangqi'
# -*- coding:utf-8 -*-

import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3307,user='spider',passwd='spider',db='spider')
cur = conn.cursor()
cur.execute("show tables;")
print(cur.description)
