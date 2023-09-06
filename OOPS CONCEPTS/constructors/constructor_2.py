#and also we can write without constructor
class Student:
 def fun1(self):
     self.sid=123
     print("Student id is:",self.sid)
     self.sname="sai"
     print("Student name is:",self.sname)
     self.saddress="hyderabad"
     
 def fun2(self):
     self.saddress="hyderabad"
     print("Student address is:",self.saddress)
     
s1=Student()
s1.fun1()
s1.fun2()
s2=Student()
s2.fun1()
s2.fun2()
