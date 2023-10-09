#Remove Duplicates from a List:
my_list = [1, 2, 2, 3, 4, 4, 5, 6]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("List with duplicates removed:", unique_list)
