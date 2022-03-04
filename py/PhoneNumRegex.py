# This program will match phone number 'xxx-xxx-xxxx', where the x is single number 
# with regular expression 

import re

PhoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = PhoneNumRegex.search("My number is 415-555-4242.")
print("My phone number is: " + mo.group(1)?)
print("Done")