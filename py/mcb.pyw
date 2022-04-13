#! python3
# mcb.pyw - Saves and loads all pieces of text to the clipboard.
# Usage:    py.exe mcb.pyw save <keywords> - Saves clipboard to keywords.
#           py.exe mcb.pyw <keywords> - Loads keywords from clipboard
#           py.exe mcb.pyw list - Loads all keywords from clipboard 

import shelve, pyperclip, sys

mcbShelve = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # Assign string of clipboard to keywords, not keywords to clipboard
    mcbShelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load contents
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelve.keys())))
    elif sys.argv[1] in mcbShelve:
        pyperclip.copy(mcbShelve[sys.argv[1]])

mcbShelve.close()
