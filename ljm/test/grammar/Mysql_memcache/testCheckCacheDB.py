#coding:utf8
from self_study.web.project.tools.cache.common_cache import cacheClient
from self_study.web.project.tools.db.biz_dbclass  import dbClient

'''检查cache和db中的数据是否一致'''
class cacheDbClient():
    
    def testCacheDb(self,executeSql,name):
        
        '''执行查询sql,从数据库中查询数据'''
        dbClientSql =  dbClient().select_data(executeSql)
        if dbClientSql <> 0:
            try:
                '''从cache中查询数据'''
                mc = cacheClient().mcget_client(name)
            except Exception,e:
                print e
                return 0
            else:
                if dbClientSql[0]<> mc:
                    print '缓存中数据和数据库数据不同，不相同的数据是： '
                    print dbClientSql[0],mc
                print '缓存中数据和数据库数据相同'
        else:
            print '数据库没有数据'
            return 0
         
if __name__ == "__main__":
    executeSqlCount = "select count(*) from user"
    dbClientSqlNum = dbClient().select_data(executeSqlCount)
    for i in range(dbClientSqlNum[0][0]):
        gid = i +1
        cacheDbClient().testCacheDb("select name,value from user where name='liangjm%s'"%gid, 'liangjm%s'%gid)