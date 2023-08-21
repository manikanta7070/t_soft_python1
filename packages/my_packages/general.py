#program for factorial of given number using functions
def factorial(n):
    if n==0:
        n=1
    else:
        n=n*factorial(n-1)
    return n

#program using alliasing of functions
def f1():  
    print("Hello")

#program for operations like sum,sub,mul,div of given numbers using functions
def operations():
    def add(x,y):
        return(x+y)
    def sub(x,y):
        return(x-y)
    def prod(x,y):
        return(x*y)
    def div(x,y):
        return(x/y)

#program for biggest number of given numbers using functions
def biggest(a,b,c):
    if a>b and a>c:
        print(a,"is big")
    elif b>c:
        print(b,"is big")
    else:
        print(c,"is big")

#program for given number is even or odd using functions
def iseven(n):
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")

#program for square of given number using functions
def square(n):
    print("square is:",n*n)
