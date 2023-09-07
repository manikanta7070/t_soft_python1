#static method
class student:
    college= "aditya"
    def __init__(self,sid,sname,saddress):
        self.sid=sid
        self.sname=sname
        self.saddress=saddress
    def display(self): #instance method recognization
        print("student details was :",self.sid,self.sname,self.saddress)
    @staticmethod  #class method recognization
    def mul(a,b): 
        print("mul is :",a*b)
    @staticmethod  #class method recognization
    def f1(): 
        print("hello")
s1=student("201","mani","kakinada")
s1.display()
s1.mul(2,3)
s1.f1()
