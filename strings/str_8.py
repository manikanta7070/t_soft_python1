#Check if a String Contains a Substring
my_string = "Hello, World!"
substring = "World"
found = False
for i in range(len(my_string) - len(substring) + 1):
    if my_string[i:i+len(substring)] == substring:
        found = True
        break
if found:
    print("Substring found")
else:
    print("Substring not found")
