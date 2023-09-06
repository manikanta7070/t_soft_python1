'''#constructor

class Student:
 def __init__(self):
     self.sid=123
     self.sname="sai"
     self.saddress="hyderabad"
 def display(self):
     print("Student id is:",self.sid)
     print("Student name is:",self.sname)
     print("Student address is:",self.saddress)
s1=Student()
s2=Student()
s1.display()
s2.display()

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


#if self was not taken
class Student:
    def __init__(x,A,y,z):
        x.sid= A
        x.sname=y
        x.saddress=z
    def display(self):
        print("Student id is:",self.sid)
        print("Student name is:",self.sname)
        print("Student address is:",self.saddress)
s1=Student("b1","mani","kakinada")
s2=Student("b0","govindsai","kirlampudi")
s1.display()
s2.display()

#method is optinal
class Student:
    def __init__(x,A,y,z):
        x.sid= A
        x.sname=y
        x.saddress=z
s1=Student("b1","mani","kakinada")
s2=Student("b0","govindsai","kirlampudi")

#o/p : not display anything
#so if you want to display anything we have to use as below

print(s1.__dict__)
print(s2.__dict__)
'''
#constructor is optional
class student:
    def data_read(self):
        self.sid = input("enter the id :")
        self.sname = input("enter the name:")
        self.saddress = input("enter the address :")
    def data_print(self):
        print(self.sid)
        print(self.sname)
        print(self.saddress)
        ##another style of printing
        print("student {} id is {} and his address is {}".format(self.sname,self.sid,self.saddress))
s1=student()
s1.data_read()
s1.data_print()

#another style of printing















