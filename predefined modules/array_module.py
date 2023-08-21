import array
 # 0 1 2 3
A=array.array('i',[10,20,30,40])
print(A)
print(type(A))
A=array.array('f',[12.3,45.6,78.9,45.2])
print(A)
print(type(A))

# to create arrays in python using array module then we use type code
from array import *
A=array('i',[10,20,30,40])
print(A)
print(type(A))
print(A.typecode)
print(A[2])
A.insert(1,34)
print(A)
A.append(45)
print(A)
A.extend([67,89,90])
print(A)
A.remove(30)
print(A)
A.reverse()
print(A)


#To display array elements using for loop:
from array import *
A=array('i',[100,200,300,400,500,600])
for i in A:
 print(i)
 
for i in range(len(A)):
 print(A[i])

 
#Copying elements from one array to another:
from array import *
A=array('i',[2,3,4,5,6])
print(A)
#B=A
#print(B)
B=array(A.typecode,[i*2 for i in A])
print(B)

#Creating array by accepting elements at runtime

from array import *
A=array('i',[])
n=int(input("Enter length of the array:"))
for i in range(n):
 x=int(input("Enter value:"))
 A.append(x)
print(A)
















