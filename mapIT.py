#! python3
#mapIt.py launches a map in the browser using address from the command line

import webbrowser,sys, pyperclip
if len(sys.argv)>1:
    #Get address from Command line
    address=''.join(sys.argv[1:])

else:    
    #Get address from Clip Board
    address=pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
