def extra_msg(printmsg):
    def inner(name):
        if name=="Raju":
            print("HEllo",name,"Good Evening")
        else:
            printmsg(name)
    return inner
        

@extra_msg
def printmsg(name):
    print("hello",name,"Good Morning")

printmsg("Balaji")
printmsg("Sai")
printmsg("Raju")
