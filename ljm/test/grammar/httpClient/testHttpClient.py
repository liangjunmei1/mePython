#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
get、post 请求
"""
import requests
import json

"""
http get 请求
r.content: 获取相应内容，以字节的方式去显示，中文显示为字符
r.text:获取相应内容，以文本的方式显示
"""
r = requests.get("http://bdimg.share.baidu.com/static/js/bds_s_v2.js?cdnversion=416138")
# print "r.content=>",r.content
# print "r.text=>",r.text

"""
http post 请求
"""
r = requests.post("http://m.ctrip.com/post")
print type(r.text)

"""
raw response context : 原始相应内容
r.raw
stream=true
"""
r = requests.get('https://api.github.com/events', stream=True)
print type(r.raw)
HTTPResponse = r.raw
# print HTTPResponse.read(20)
with open("rawResult.txt", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

"""
headers 请求
"""
url = 'https://developer.github.com/v3'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url)
# print r.text

"""
post 请求

json.dumps: dict转成str
json.loads: str转成dict
"""
payload = {'key1': 'value1', 'key2': 'value2'} # dict
# payload = (('key1', 'value1'), ('key1', 'value2')) #tuple 类型

# r = requests.post("http://httpbin.org/post",data=payload)
r = requests.post("http://httpbin.org/post",data=json.dumps(payload))
# print r.text
print r.status_code
print r.status_code == requests.codes.ok
print r.raise_for_status()   # 状态失败抛出异常

"""
得到请求的 header、cookies
"""
print r.headers
print r.cookies

