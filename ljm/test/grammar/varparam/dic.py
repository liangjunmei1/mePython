#encoding:utf-8
'''
Created on 2017-1-13

@author: Administrator
'''

# 词典是没有顺序的
dic = {'tom':'111','lili':'222','haha':'222'}
print dic.keys()
print dic.values()
print dic.items()
#print dic.clear()
print type(dic)

#引用
print dic['tom']
#增加新元素
dic['ljm'] = 333
print dic

#循环调用dic
for key in dic:
    print dic[key]
    
del dic['haha']
print dic
print len(dic)