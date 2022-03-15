#Adds * to the lines copied using split and join method

import pyperclip as pc

text = pc.paste()

linelist= text.split('\n')
for i in range(len(linelist)):
    linelist[i]='*'+linelist[i]

text='\n'.join(linelist)
pc.copy(text)