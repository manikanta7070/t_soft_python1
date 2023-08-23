#excetion handling
"""
from math import sqrt
a=10
try:
    b=sqrt(a)
    print("sqrt is",b)
except 
print("a value is",a)
print("Welcome to python world")

"""

from math import sqrt 
try:
    l=[10,0]
    b=sqrt(l[1]) #sqrt(-10) # Sqrt(l[2])
    print("sqrt is",b) #print(c)
    b=l[0]/l[1]
    print("Division is",b)
except ZeroDivisionError as e:
    print("Divisor not to be a zero",e)
except NameError as e:
    print("Name Error message is",e)
except ValueError as e:
    print("Value Error message is",e)
except IndexError as e:
    print("Index Error message is",e)
except Exception as e:
    print("Generic Exception",e)
else:
    print("\n there are no exception")
    
finally:
     print("\n Finally block will execute Irespective the exception")


print("a value is",l)
print("Welcome to python world")
