#OOPs
#=======
#x is a golbal variable so we can't restrict it from accessing from the specific function
x=10

def f1():
    a=100
    print("a=",a)
    print("x=",x)

def f2():
    b=200
    print("b=",b)
    print("x=",x)

def f3():
    c=300
    k=500
    print("c=",c)
    print("k=",k)
    print("x=",x)    


f1()
f2()
f3()

class sample:
    x=10           #class variables or attributes
    def f1(self):  #methods
        a=100      # local to method f1
        print("a=",a)
        print("x=",sample.x)
    def f2(self):    #method
        b=200        # local variable to f2
        print("b=",b)
        print("x=",sample.x)
    def f3(self):
        print("Current Object is",self)
        self.f1()
        self.f2()
        

# x f1 and f2 are called members of a class sample
# will use . operator to access the members of a class. it(.) is member accessing operator 
obj=sample()
obj.f3()
print("x value is",obj.x)



class test:
#data memebers and function memebers
    def read_data(self):
        test.a=eval(input("Enter a value"))
        test.b=eval(input("Enter b Value"))
    def print_data(self):
        print("A value is",test.a)
        print("B value is",test.b)
    def __init__(self):
        a=0
        b=0
        print("\n I am in constructor menthod")
        print("a=",a,"b=",b)
            
test_obj=test()
test_obj.read_data()
test_obj.print_data()



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









