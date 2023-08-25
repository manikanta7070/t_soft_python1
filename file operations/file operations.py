#Properties of File Object:
#readable()
#readable()
f=open("sample.txt","w")
print("file name is:",f.name)
print("file mode is:",f.mode)
print("is file readable?",f.readable())
print("is file writable?",f.writable())
print("is file closed?",f.closed)
f.close()
print("is file closed?",f.closed)

f=open("sample.txt","a+")
print("file name is:",f.name)
print("file mode is:",f.mode)
print("is file readable?",f.readable())
print("is file writable?",f.writable())
print("is file closed?",f.closed)
f.close()
print("is file closed?",f.closed)


#The with statement:


with open("abcd2.txt","w") as f:
 f.write("Hello\n")
 f.write("Hyderabad\n")
 print("is file closed?",f.closed)
 
print("is file closed?",f.closed)


with open("abcd2.txt","r") as f:
    print(f.read())
    print("is file closed?",f.closed)

print("is file closed?",f.closed)

with open("abcd2.txt","w") as f:
 f.write("Hello\n")
 f.write("Hyderabad\n")
 print("is file closed?",f.closed)
 
print("is file closed?",f.closed)


with open("abcd2.txt","r") as f:
    print(f.read())
    print("is file closed?",f.closed)

print("is file closed?",f.closed)

#Seek and Tell Methods:

with open("abcd2.txt","r") as f:
    print(f.tell())  #0
    print(f.read(6))  #Hello\n"
    print(f.tell())  # 7
    print(f.seek(0))  #0
    print(f.read(3))  #Hel

    print("is file closed?",f.closed)

print("is file closed?",f.closed)




















