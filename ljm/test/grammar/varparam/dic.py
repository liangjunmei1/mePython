#encoding:utf-8
'''
Created on 2017-1-13
@author: Administrator
'''

# 词典是没有顺序的
dic = {'tom':'111','lili':'222','haha':"{'ha':'333'}"}
# print dic.keys()
# print dic.values()
# print dic.items()
# print dic.clear()
# print type(dic)
print dic['tom'] #引用
# dic['ljm'] = 333  #增加新元素

for key in dic: #循环调用dic
    # print key,dic[key]
    print key

# del dic['haha']
# print len(dic)

def conKeys(dic,str):
    boo = dic.get(str)