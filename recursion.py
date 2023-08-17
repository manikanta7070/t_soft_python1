
#factorial progam

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")


#2 sumof N natural numbers
    
def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)

# Test the function
num = int(input("Enter a positive integer: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_natural_numbers(num)
    print(f"The sum of the first {num} natural numbers is {result}")



#3
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Test the function
num = int(input("Enter the number of Fibonacci numbers to generate: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(num)
    print("Fibonacci Series:", result)



def fact1(n):
    if n==0:
        return(1) 
    else:
        return (n * fact1(n-1))


def fact2(n):
    if n>0:
        return (n * fact2(n-1))
    else:
        return (1)
n=eval(input("Enter a number"))
print("Factorial of {} is {} ".format(n,fact1(n)))
print("Factorial of {} is {} ".format(n,fact2(n)
    
	
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))

for i in range(10):
    print(fib(i),end=" ")
		

def gcd(a,b):  # gcd(8,36) # gcd(36,4) # gcd(4,0)
    if(b==0):
        return a
    else:
        return gcd(b,a%b)  # gcd(36,4) # gcd(4,0)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("GCD of {} and {} is {}: ".format(a,b,gcd(a,b)))

# Recursion for finding the sum of digits of a number

l=[]
def sum_digits(b):
    if(b==0):
        return l
    dig=b%10
    l.append(dig)
    sum_digits(b//10)
n=int(input("Enter a number: "))
sum_digits(n)
print(sum(l))
