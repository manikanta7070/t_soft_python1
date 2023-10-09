#Filter Even Numbers in a List:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []
for item in my_list:
    if item % 2 == 0:
        even_numbers.append(item)
print("Even numbers:", even_numbers)
