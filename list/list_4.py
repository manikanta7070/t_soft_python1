#Count Occurrences of an Element in a List
my_list = [1, 2, 2, 3, 2, 4, 2, 5]
count = 0
element_to_count = 2
for item in my_list:
    if item == element_to_count:
        count += 1
print(f"{element_to_count} occurs {count} times.")

