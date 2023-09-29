import re

pattern = r'(apple|banana)'
string = 'I have an apple and a banana.'
#string = 'i have an apple and a banana.'
matches = re.findall(pattern, string)
print (matches)
