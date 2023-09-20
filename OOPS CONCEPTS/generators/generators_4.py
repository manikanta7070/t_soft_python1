def countdown(n):
    while n > 0:
        yield n
        n -= 1


# Using the generator in a loop
print(type(countdown))
for num in countdown(5):
    print(num)

