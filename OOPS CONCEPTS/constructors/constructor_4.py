#parameters  name should not same as variables
class Student:
 def __init__(self,x,y,z):
     self.sid= x
     self.sname= y
     self.saddress=z
 def display(self):
     print("Student id is:",self.sid)
     print("Student name is:",self.sname)
     print("Student address is:",self.saddress)
s1=Student("b1","mani","kakinada")
s2=Student("b0","govindsai","kirlampudi")
s1.display()
s2.display()
