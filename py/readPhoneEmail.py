# python3 
# readPhoneEmail program will find phone number and email address from clipboard, and copy these phone numbers
# and emall address from clipboard paste into clipboard. 

import re, pyperclip

# define phone regular expression
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area xxx or (xxx)
    (\s|-|\.)?   # seperator space, dash, and dot
    (\d{3})     # three number
    (\s|-|\.)    # seperator
    (\d{4})      # four number
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension space + ext or x or extsomething + space + xx-xxxxx number
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  #username include all these characters without metacharacters
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name 
    (\.[a-zA-Z]{2,4})   # dot-something: can be co, coom. 
    )''', re.VERBOSE)

# Find matches in clipboard text. 
text = str(pyperclip.paste()) # pyerclip.paste give a string from clipboard to text variable
matches = [] # matches is a list waiting for phone and email added.
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text): 
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches)) # move matches list to the clipboard, seperated with new line. 
    print('Copied to clipboard:')
    print('\n'.join(matches)) # print what was copied in the screen. 
else:
    print('No phone numbers or email addresses found.')

# Example:
# From clipboard:(input)
# Copied to clipboard: 800-420-7240       ext.     2223 415-863-9900 asdfas 415-863-9950 asdf ext 234 info@nostarch.com media@nostarch.com 
# academic@nostarch.com help@nostarch.com asd@s.co asdfasdf
# 
# print in the screen:(output)
# 800-420-7240 x2223
# 415-863-9900
# 415-863-9950
# info@nostarch.com
# media@nostarch.com
# academic@nostarch.com
# help@nostarch.com
# asd@s.co