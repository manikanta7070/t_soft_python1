#programs under functions in modules
from my_packages.arithmatic import *
add(10,20)
mul(30,20)
sub(50,20)
div(10,5)
rem(8,6)

#programs under functions from general modules
from my_packages.general import *
print(factorial(6))
f1()
biggest(10,20,30)
iseven(8)
square(5)

#programs under functions using tuples in modules
from my_packages.tuple import *
s=read_data_tuple()
print(s)
print("Max Mark marks is:",max_marks(s))
print("Min Mark marks is:",min_marks(s))
print("Total marks is:",sum_marks(s))

#programs under functions using sets in modules
from my_packages.set import *
s=read_data_set()
print(s)
print("Max Mark marks is:",max_marks(s))
print("Min Mark marks is:",min_marks(s))
print("Total marks is:",sum_marks(s))

#programs under functions using list in modules
from my_packages.list import *
L=Read_list_values()
print("Max of list items is ",max(L))
print("Min of list items is",min(L))
print("Sum of list items is",sum(L))

#programs under functions using list in modules
from my_packages.strings import *
result0=palindrome(N)
if result0==temp0:
    print("palindrome number")
else:
    print("Not palindrome number")

#programs under functions using list in modules
from my_packages.strings import *
result1=perfect_number(N1)
if result1==temp1:
    print("perfect number ")
else:
    print("Not perfect number ")

#programs under functions using list in modules
from my_packages.strings import *
result2=armstrong(N2)
if result2==(2*N2):
    print("ArmStrong")
else:
    print("Not a ArmStrong")
