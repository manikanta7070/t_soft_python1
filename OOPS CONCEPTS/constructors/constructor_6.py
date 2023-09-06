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

'''print(s1.__dict__)
print(s2.__dict__)''
