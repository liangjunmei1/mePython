#coding:utf-8

#继承  父类
class SchoolMember(object): 
    '''Represents any school member.''' 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
        print '(Initialized SchoolMember: %s)' % self.name 
        
    def tell(self):                        
        print 'name:"%s" '  %self.name,'age: "%s"'  %self.age
        