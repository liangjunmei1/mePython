#coding:utf-8

from InheritParent  import SchoolMember

class Teacher(SchoolMember):
    '''Represents a teacher.''' 
     
    def __init__(self, name, age, salary): 
        SchoolMember.__init__(self, name, age) 
        self.salary = salary 
        print '(Initialized Teacher: %s)' % self.name 
         
    def tell(self): 
        SchoolMember.tell(self) 
        print 'Salary: "%d"' % self.salary 
        

class Student(SchoolMember): 
    def __init__(self, name, age, score): 
        SchoolMember.__init__(self, name, age) 
        self.scroe = score 
        
'''子类继承父类，自动拥有了父类的方法'''
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75) 
t.tell() 
s.tell()
    
