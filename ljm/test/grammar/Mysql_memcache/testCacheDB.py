#coding:utf8
from self_study.web.project.tools.cache.common_cache import cacheClient
from self_study.web.project.tools.db.biz_dbclass  import dbClient

class cacheDbClient():
    
    def testCacheDb(self,executeSql,gid,sqlData):
        print executeSql,gid,sqlData
        dbClientNum = dbClient().insert_data(executeSql)

        '''执行sql，插入成功，向cache中写数据'''
        if dbClientNum == 1:
            try:
                mc = cacheClient().mcset_client(gid, sqlData)
            except Exception,e:
                print e
                return 0
            else:
                if mc <> 1:
                    return 0
                return 1
        else:
            return 0
        
if __name__ == "__main__":
    for i in range(2):
        gid = i+1
        sqlData = ("liangjm%s"%gid,gid)
        executeSql = "insert into user(name,value) values('%s','%s')"%sqlData
        
        print cacheDbClient().testCacheDb(executeSql,"liangjm%s"%gid, sqlData)
