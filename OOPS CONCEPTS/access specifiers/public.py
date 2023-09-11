class details:
      
     # constructor
     def __init__(self, name, age):
           
           # public data members
           self.myName = name
           self.myAge = age
 
     # public member function     
     def displayAge(self):
           
           # accessing public data member
           print("Age: ", self.myAge)
 
# creating object of the class
obj = details("R2J", 20)
 
# accessing public data member
print("Name: ", obj.myName)
 
# calling public member function of the class
obj.displayAge()
