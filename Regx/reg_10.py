#pattern matching

import re

pattern = r'^[A-Za-z]+\d+$'
string = 'hello123'

if re.match(pattern, string):
    print('pattern matched!')
else:
    print('pattern not matched.')
