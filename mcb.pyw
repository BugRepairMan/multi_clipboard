#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys 

mcbShelf = shelve.open('mcb.db')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        all_keys = str(list(mcbShelf.keys()))
        print('KEYS to clipboard: ' + all_keys)
        pyperclip.copy(all_keys)
    elif sys.argv[1] in mcbShelf:
        key = sys.argv[1]
        content = mcbShelf[key]
        print('Content to clipboard:\n' + content)
        pyperclip.copy(content)

mcbShelf.close()
