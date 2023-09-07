#Instance methods
#note : pass self as first parameter and
#inside the method implementation we should use instant varaiables 
class student:
    def __init__(self,sid,sname,saddress):
        self.sid=sid
        self.sname=sname
        self.saddress=saddress
    def display(self): #instance method
        print("student details was :",self.sid,self.sname,self.saddress)
s1=student("201","mani","kakinada")
s2=student("200","govind","kirlampudi")
s1.display()
s2.display()
