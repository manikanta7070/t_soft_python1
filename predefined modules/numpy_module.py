#Examples with numpy arrays:
#Ex1:
import numpy
#A=numpy.array([10,20,30,40,50])
A=numpy.array([10,20,30,40,50.8],int)
print(A)
print(type(A))
print(A.dtype)
print(A.ndim)
print(A.size)
print(A.shape)


#Ex2:
from numpy import *
A=linspace(2,20,7)#start,stop,no of parts
print(A)
A=logspace(3,15,6)
print(A)
A=arange(2,20,3)#start,stop,step
print(A)
A=zeros(6,int)
print(A)
A=ones(6,int)
print(A)


#Ex3:
import numpy as np
A=np.array([[10,20,30],[34,56,78],[78,23,45]])
print(A)
print(A.dtype)
print(A.ndim)
print(A.shape)
print(A.size)

#Ex4:
import numpy as np
A=np.array([[-10,20,30],[34,-56,78],[78,23,-45]])
print("max element is:",A.max())
print("min element is:",A.min())
print("col wise max element is:",A.max(axis=0))
print("col wise min element is:",A.min(axis=0))
print("row wise max element is:",A.max(axis=1))
print("row wise min element is:",A.min(axis=1))
print(A.sum())


#flatten () method:

A=np.array([[-10,20,30],[34,-56,78],[78,23,-45]])
print(A)
print(A.ndim)
B= A.flatten()
print(B)
print(B.ndim)






















print(A[1][2])
