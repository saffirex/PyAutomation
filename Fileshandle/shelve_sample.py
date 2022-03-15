import shelve
from pathlib import Path as p
shelffile= shelve.open(str (p.cwd() / 'target_folder'/ 'new'))
names= ['one','safal','five','seven']
shelffile['namesofperson']= names
print(shelffile['namesofperson'])
shelffile.close()