'''import time
class Test:
 def __init__(self):
     print("Constructor execution")
 def __del__(self):
     print("Destructor execution")
t=Test()'''

#time.sleep(5)

#2
import time
class Test:
 def __init__(self):
     print("Constructor execution")
 def __del__(self):
     print("Destructor execution")
l=[Test(),Test(),Test()]
time.sleep(5)
del l
print("end of program")
