#coding:utf-8

class interface(object): 
    def run(self,a): 
        self.start(a) 
        self.process(a) 
        self.end(a) 
    
    def start(self,a):
        pass 
    def process(self,a): 
        pass 
    def end(self,a): 
        pass
    
class I1(interface): 
    
    def start(self,a): 
        print 'start',a 
    
    def process(self,a): 
        print 'process',a 
    
    def end(self,a): 
        print 'end',a 
        
x=I1() 
x.run(123) 
y=interface() 
y.run(1)
        