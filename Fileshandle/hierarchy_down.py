from pathlib import Path as path
import os
print(path.cwd())
foldername=path('new_folder_making')
newpath = path.cwd() / foldername
print (newpath)
#homedirectory
print(path.home())