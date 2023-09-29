#splitting

import re

pattern = r'\s'
string = 'hello    world welcome to python'

tokens = re.split(pattern, string)
print(tokens)
print("no of words",len(tokens))
