'''class Test:
 def __init__(self):
     self.a=10
     self.b=20
     self.c=30

t1=Test()
t2=Test()
print(t1.__dict__)
print(t2.__dict__)

#now examples to delete instance varaiabes
#within the class

class Test:
 def __init__(self):
     self.a=10
     self.b=20
 def m1(self):
     del self.a #this is the way we use write instruction
t1=Test()
t2=Test()
print(t1.__dict__)
print(t2.__dict__)
t1.m1()
print(t1.__dict__)
print(t2.__dict__)#ptinting after deleting

#oustside the class

class Test:
 def __init__(self):
     self.a=10
     self.b=20
t1=Test()
t2=Test()
print(t1.__dict__)
print(t2.__dict__)
del (t1.b,t2.b)        #this is the way we use write instruction
print(t1.__dict__)
print(t2.__dict__)#printing after deleting'''

#changes 

class Test:
 def __init__(self):
     self.a=10
     self.b=20
 def m1(self):
     self.a=90
t1=Test()
t2=Test()
print(t1.__dict__)
print(t2.__dict__)
t2.b=66
t1.m1()
print(t1.__dict__)
print(t2.__dict__)






















