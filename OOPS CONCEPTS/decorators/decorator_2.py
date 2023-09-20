def mydiv(div):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return div (x,y)
    return inner
@mydiv
def div(a,b):
    return (a/b)

print(div(2,4))
print(div(4,2))

