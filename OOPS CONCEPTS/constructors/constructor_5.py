#if self was not taken the start parameter x consider as self 
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
