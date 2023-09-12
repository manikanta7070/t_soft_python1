class Test:
 x=10 #public
 _y=20 #protected
 __z=30 #private
 def __init__(self):
     print("within the class")
     print(self.x)
     print(self._y)
     print(self.__z)
     t=Test()
     print("outside of the class")
     print(t.x)
     print(t._y)
     print(t.__z) #AttributeError: 'Test' object has no attribute '__z'

#2
class Parent:
 x=10 #public
 _y=20#protected
 __z=30 #private
class Child(Parent):
    print(Parent.x)
    print(Parent._y)
 #print(Parent.__z) #AttributeError: type object 'Parent' has no attribute '_Child__z'
c=Child()

#3
class Car:
 def __init__(self):
     self.__updatesoftware()
 def __updatesoftware(self): #private method
     print("Updating software")
 
c=Car()
#c.__updatesoftware() #AttributeError: 'Car' object has no attribute '__updatesoftware'



#4
class Car:
 __name=""
 __maxspeed=0
 def __init__(self):
     self.__name="verna"
     self.__maxspeed=100
     print(self.__name)
     print(self.__maxspeed)
 def drive(self):
     self.__maxspeed=200
     print("Driving")
     print(self.__name)
     print(self.__maxspeed)
c=Car()
#c.__maxspeed=200 #maxspeed will not change
c.drive()
































