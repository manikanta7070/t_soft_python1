#in the above program "__init__" is the constructor with "self"
#as a primary parameter
#Constructor is a special method of class.

#constructor with parameters
class Student:
 def __init__(self,sid,sname,saddress):
     self.sid= sid
     self.sname=sname
     self.saddress=saddress
 def display(self):
     print("Student id is:",self.sid)
     print("Student name is:",self.sname)
     print("Student address is:",self.saddress)
s1=Student("b1","mani","kakinada")
s2=Student("b0","govindsai","kirlampudi")
s1.display()
s2.display()
