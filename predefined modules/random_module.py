#Functions of random module:
#1. Random()
#2. Randint()
#3. Uniform()
#4. Randrange()
#5. Choice()

#random
from random import *
for i in range(5):
 print(random())
 
#Randint () :
from random import *
for i in range(10):
#print(randint(2,21))
 print(randint(1000,2000))
 
#Uniform () :
from random import *
for i in range(10):
 print(uniform(2,21))

#andrange () :
from random import *
for i in range(10):
 print(randrange(2,21,3))


#Choice ():

from random import *
l=["sai","mohan","raj","ram",10,34.5,"manoj"]
x=choice(l)
print(x)
print(type(x))
#in python everything is called as object




















