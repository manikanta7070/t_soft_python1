#substitution

import re

pattern = r'butter'
string = ' i love peanut butter on my toast.'

new_string = re.sub(pattern, 'jam', string)
print(new_string)
