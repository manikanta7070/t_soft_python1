#1
class Outer:
 def __init__(self):
     print("Outer class constructor")
 def f1(self):
     print("outer class method")
 class Inner:
     def __init__(self):
         print("Inner class constructor")
     def m1(self):
         print("Inner class method")
'''o=Outer()
i=o.Inner()
i.m1()'''
'''i=Outer().Inner()
i.m1()'''
#Outer().Inner().m1()
o=Outer()
o.f1()
i=o.Inner()
i.m1()
