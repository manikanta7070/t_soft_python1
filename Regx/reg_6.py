import re

pattern = r'\d{1,3}'#for two digits

string = "The recipe requires 2 cups of flour and 3 eggs."
string = "The recipe requires 12 cups of flour and 35 eggs."

matches = re.findall(pattern, string)
print(matches)#output: ['2', '3']
