from pathlib import Path as p
import os

for root,sub,files in os.walk(p.cwd()):
    print(root)
    for subfolders in sub:
        print('\t',subfolders)
    print('\n')
    for filenames in files:
        print('\t\t',filenames)
    print('\n')


