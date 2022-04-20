#! python3
# mapIt.py - Launch a map using browser from command line 
# or clipboard.

import sys, webbrowser, pyperclip

# Concatenate string from command line arguments
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
# Copy string from clipboard
else:
    address = pyperclip.paste()

# Open map 
webbrowser.open('https://www.google.com/maps/place/' + address)