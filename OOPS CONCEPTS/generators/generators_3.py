def f1():
    yield "Sai"
    yield 123
    yield "SaiRam"
    yield 123.45

print(type(f1))
for i in f1():
    print(i)
