
def display():
    number=10
    #print(number)
    number+=10
    #print(number)
    yield number
    number+=10
    yield number
    number+=10
    yield number
    number+=10
    yield number
    
    
"""    
result=display()
print(next(result))
print(next(result))
print(next(result))
print(next(result))
"""

for result in display():
    print(result)
