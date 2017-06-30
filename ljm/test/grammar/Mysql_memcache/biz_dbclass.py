#coding:utf8
import MySQLdb,os
'''函数封装成class'''
class dbClient():

    def __init__(self,host='10.10.10.61',user='root',passwd='root',db='core',port=3306,charset="utf8"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db
        self.charset = charset
        try:
            self.conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,port=self.port,db=self.db,charset=self.charset)
        except MySQLdb.Error as e:
            print e
            os._exit(0)
        else:
            '''得到游标'''
            self.cur = self.conn.cursor()

    '''insert 单条记录'''
    def insert_data(self,sql):
        try:
            self.cur.execute(sql)
        except MySQLdb.Error as e:
            print '添加数据失败'
            print e
            return 0
        else:
            self.conn.commit()
            print '添加数据成功'
            return 1
        finally:
            self.cur.close()
            self.conn.close()

    '''查询sql'''
    def select_data(self,sql):
        try:
            self.cur.execute(sql)
        except MySQLdb.Error as e:
            print '查询数据失败'
            print e
            return 0
        else:
            results = self.cur.fetchall()
            return results
            print '查询数据成功'
        finally:
            self.cur.close()
            self.conn.close()


#dbClient().insert_data("insert into test(name,value) values('ljm2','2')")
result = dbClient().select_data("select * from test where name = 'ljm2'")
print result
