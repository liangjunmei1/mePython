#coding:utf-8

'''
                文件IO
打开 open(filename[, mode[, buffersize])
        f = open("foo","w")         # Open a file for writing or file(‘foo’,’w’)
        g = open("bar","r")         # Open a file for reading or file(‘foo’,’r’)
读取 read([nbytes]), readline(), readlines()
        data = g.read() # Read all data
        line = g.readline() # Read a single line
        lines = g.readlines() # Read data as a list of lines
        注：readlines不会trim末尾的换行字符
写入 write(string), writelines(list)
        f.write("Hello World")
        f.writelines([“af”,‘;afd’]) # 注：list 元素必须是str
定位   seek(pos[, how]), tell()
关闭   f.close()
'''

'''
pickle是为了序列化/反序列化一个对象的，可以把一个对象持久化存储。
比如你有一个对象，想下次运行程序的时候直接用，可以直接用pickle打包存到硬盘上。或者你想把一个对象传给网络上的其他程序，可以用pickle打包，然后传过去，那边的python程序用pickle反序列化，就可以用了。
    pickle.dump(obj, file, [,protocol])    注解：将对象obj保存到文件file中去。
    pickle.load(file)             注解：从file中读取一个字符串，并将它重构为原来的python对象。
'''
import pickle 

list1 = [1,2,3] 
data1 = {'a': [1, 2.0, 3, 4+6j], 'b': ('string', u'Unicode string'), 'c': None, 'd': list1 } 

output = open('data.pkl', 'wb') 
pickle.dump(data1, output) 
output.close()
    
infile = open('data.pkl','rb') 
newData1 = pickle.load(infile) 
print newData1
    
