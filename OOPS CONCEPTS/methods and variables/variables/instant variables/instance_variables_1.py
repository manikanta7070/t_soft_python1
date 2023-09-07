#instance variables can be called as object level variables
class Test:
 def __init__(self):
     self.a=10  #declare within the class using self
 def m1(self):
     self.b=20   #declare within the method using self
t=Test()
t.m1()
t.c=30 # declare outside the class with object reference varaiable name
print(t.__dict__)
