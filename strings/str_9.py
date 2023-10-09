#Find the Most Common Character in a String
my_string = "Hello, World!"
char_count = {}
for char in my_string:
    if char.isalpha():
        char_count[char] = char_count.get(char, 0) + 1
most_common_char = max(char_count, key=char_count.get)
print("Most common character:", most_common_char)
