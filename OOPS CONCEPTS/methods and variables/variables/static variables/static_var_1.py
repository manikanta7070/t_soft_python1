#static varibles also called as class level variables
'''class Mani :
    a=10 #static declaration ,and declaration should be outside of method.
    def __init__(self):
        self.b=20
n1=Mani()
n2=Mani()
print(n1.a,n1.b)
print(n2.a,n2.b)'''

#effects due to change of static variable.
class Mani():
    a=20
    def __init__(self):
        self.b=22

n1=Mani()
n2=Mani()
print(n1.a,n1.b)
print(n2.a,n2.b)
print("after changes ")
Mani.a=99
print(n1.a,n1.b)
print(n2.a,n2.b)
