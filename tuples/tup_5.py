#Search for an Element in a Tuple
my_tuple = (10, 20, 30, 40, 50)
search_item = 30
found = False
for item in my_tuple:
    if item == search_item:
        found = True
        break
if found:
    print(f"{search_item} found in the tuple.")
else:
    print(f"{search_item} not found in the tuple.")

