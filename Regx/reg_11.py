#pattern matching

import re

pattern = r'^d{3}-\d{3}=\d{4}$'
phone_number = 'number is 123-456-7890'

if re.match(pattern, phone_number):
    print('phone number valid!')
else:
    print('phone number not valid.')
