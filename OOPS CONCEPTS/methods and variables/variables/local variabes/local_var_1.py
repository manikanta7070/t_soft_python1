'''class Mani :
    def __init__(self):
        self.a=23
    def m1(self):
        b=20
        print(b)
    def m2(self):
        c=30
        print(c)
n1=Mani()
print(n1__dict__)
n1.m1()
n1.m2()'''

#now we try to access "b" varaible in m2 method and "c" in m1 method 
class Mani :
    def __init__(self):
        self.a=23
    def m1(self):
        b=20
        print(b)
        print(c)
    def m2(self):
        c=30
        print(c)
        print(c)
n1=Mani()
n1.m1()
n1.m2()
#the o/p shows c is not defined 



