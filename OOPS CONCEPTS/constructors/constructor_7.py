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
