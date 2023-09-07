#class method '
#we should use decorator to represent class method i.e,@classmethod ,before the method declaration
class student:
    college= "aditya"
    def __init__(self,sid,sname,saddress):
        self.sid=sid
        self.sname=sname
        self.saddress=saddress
    def display(self): #instance method recognization
        print("student details was :",self.sid,self.sname,self.saddress)
    @classmethod  #class method recognization
    def method(self): 
        print(self.college)
s1=student("201","mani","kakinada")
s2=student("200","govind","kirlampudi")
s1.display()
s2.display()
s1.method ()
s2.method()

