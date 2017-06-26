#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
json.dumps: 将 Python 对象编码成 JSON 字符串
json.loads: 将 已编码成 json字符串 解析成 python 对象
"""
"""
encode	将 Python 对象编码成 JSON 字符串
decode	将 已编码的 JSON 字符串解码为 Python 对象

"""
import json
import demjson  # 第三方jar包

data = [{'a':1,'b':2,'c':3 ,'d':4,'e':5}]
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

print type(data),type(json.dumps(data))
print json.dumps(data)
print demjson.encode(data)


print demjson.decode(jsonData)
print json.loads(jsonData)


