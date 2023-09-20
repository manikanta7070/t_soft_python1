#genarator are defined using functions with the yield keyword
def display ():
    a=10
    b=20
    return a+b
    a=100
    b=200
    return a+b
    a=1000
    b=2000
    return a+b
result= display()
print(result)

#in the above program if we call the function it will diplay output on 30
#because of the return statement terminates the function after its execution.

#so we use "yeild" keyword

def display ():
    a=10
    b=20
    yield a+b
    a=100
    b=200
    yield a+b
    a=1000
    b=2000
    yield a+b
'''    
result= display()
print(result)
print(next(result))
print(next(result))
print(next(result))'''

#or we can write using for loop also

for result in display():
    print(result)























