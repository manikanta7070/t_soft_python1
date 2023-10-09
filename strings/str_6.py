#Remove Spaces from a String
my_string = "   This is a string with spaces   "
no_spaces_string = ""
for char in my_string:
    if char != " ":
        no_spaces_string += char
print("String with spaces removed:", no_spaces_string)
