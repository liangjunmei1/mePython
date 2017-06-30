#coding:utf8
import memcache
class cacheClient():

    def __init__(self):
        self.memp_ip = "127.0.0.1:11211"

    def mcset_client(self,key,value):
        try:
            mc = memcache.Client([self.memp_ip])
        except Exception,e:
            print e
            print '写入缓存失败'
            return 0
        else:
            print mc
            result = mc.set(key,value)
            print result
            if not result:
                return '写入缓存失败'
            return '写入缓存成功'

    def mcget_client(self,key):
        try:
            mc = memcache.Client([self.memp_ip])
        except Exception,e:
            print e
            return 0
        else:
            result = mc.get(key)
            if result == None:
                print key
                return
            return result

    def mcdelete_client(self,key):
        try:
            mc = memcache.Client([self.memp_ip])
        except Exception,e:
            print e
            return 0
        else:
            result = mc.delete(key);
            if not result:
                return 0
            return 1

#print cacheClient().mcset_client("ljm","ljm")
#print cacheClient().mcget_client("ljm")
#print cacheClient().mcdelete_client("liangjunmei_1")
