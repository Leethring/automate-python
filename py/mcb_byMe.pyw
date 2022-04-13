#! python3 
# mcb_byMe.pyw - Save and load my clipboard 
# Useage:   python mcb_byMe.pyw save <keywords> - Saves clipboard to keywords
#           python mcb_byMe.pyw <keywords> - Loads keywords from clipboard list
#           python mcb_byMe.pyw list - Loads all keywords from clipboard list

import shelve, sys, pyperclip

myShelf = shelve.open('mcb_byMe')

# Save clipboard to keywords
if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
    myShelf[sys.argv[2]] =  pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        # Print a list of keys
        print(str(list(myShelf.keys())))
    elif sys.argv[1] in myShelf:
        pyperclip.copy(myShelf[sys.argv[1]])

# todo: Load keywords from clipboard
myShelf.close()