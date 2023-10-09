#Count the Number of Digits in a String
my_string = "12345abcde67890"
digit_count = 0
for char in my_string:
    if char.isdigit():
        digit_count += 1
print("Number of digits in the string:", digit_count)
