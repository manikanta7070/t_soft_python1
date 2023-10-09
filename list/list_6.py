#Find the Index of an Element in a List
my_list = [10, 20, 30, 40, 50]
element_to_find = 30
index = -1
for i in range(len(my_list)):
    if my_list[i] == element_to_find:
        index = i
        break
print(f"Index of {element_to_find}: {index}")
