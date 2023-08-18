#lambda 
s=lambda n: n*n
print( "square is :",s(4))
s=lambda a,b: a if a>b else b
print("the largest number is :",s(23,45))
s=lambda c,d:c+d
print("sum is :",s(2,3))
s=lambda j,k,l:j if j>k and j>l else k if  k>l else l
print("the largest number is :",s(3,9,8))


#filter() is usedto filter the values based on conditio from given sequence
l= [2,3,4,3,6,9]
l2= list(filter(lambda x:x%2==0,l))
print("even number are :",l2)


#map()
l= [2,3,4,3,6,9]
l2= list(map(lambda x:x*x,l))
print("the list with sqares was :",l2)

#map on two list

l= [2,3,4,3,6,9]
l2= list(map(lambda x:x*x,l))
print("the list with sqares was :",l2)

#reduce()
from functools import *
l= [2,3,4,3,6,9]
result=reduce(lambda x,y:x+y,l)
print(result)


#2
from functools import *
l= [2,3,4,3,6,9]
result=reduce(lambda x,y:x-y,l)
print(result)

#3
from functools import *
l= [2,3,4,3,6,9]
result=reduce(lambda x,y:x*y,l)
print(result)

















