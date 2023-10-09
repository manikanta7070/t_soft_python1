#Find the Maximum Element in a List
my_list = [17, 12, 25, 8, 41]
max_value = my_list[0]
for item in my_list:
    if item > max_value:
        max_value = item
print("Maximum value:", max_value)
