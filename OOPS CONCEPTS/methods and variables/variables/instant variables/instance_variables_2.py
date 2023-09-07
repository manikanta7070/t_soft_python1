#instance variables can be called as object level variables
class Test:
 def __init__(self):
     self.a=10
     self.b=20 #declaration instace variables 
 def m1(self):
     print(self.a)
     print(self.b)   #access within the method using self
t=Test()
print(t.a) # access outside the class with object reference varaiable name
print(t.b)
t.m1()

