#modules
# step 1 :for example now i was creating programs and each would be cosidering  as single moudle
#step : 2 those two modules had created as sample and sample1 and i want to use those two modules
#in another program so i have to import those modules and it has different ways .
#working using import sample module
import add_sub
import multiply
print(add_sub.a)
add_sub.add(20,30)
add_sub.sub(30,19)
print(multiply.a)
multiply.mul(2,3)
#if i don't want to repeat module name then use othe mode
from add_sub import *
print(a)
add(2,3)
sub(10,5)
from multiply import *
print(a)
mul(4,5)

#module names aliasing
import add_sub as s
import multiply as m
print(s.a)
s.add(20,30)
s.sub(30,19)
print(m.a)
m.mul(2,3)

#we can access members directly without using module name.
from sample import x,add,mul
print(x)
add(10,20)
mul(20,30)

from sample import *
print(x)
add(10,20)
mul(20,30)

#Working with math module: 
from math import *
print(factorial(3))
print(sqrt(4))
print(pow(3,2))
print(log(10,2))
print(ceil(34.2))
print(floor(34.9))

#Working with random module:


#members aliasing
from add_sub import * add as sum ,a as k
print(add_sub.k)
add_sub










