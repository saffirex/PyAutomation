import zipfile, os
from pathlib import Path as path
print(path.cwd())
os.chdir(path.cwd() / 'testfolder' )
print(path.cwd())

for filenames in path.cwd().glob('new?.txt'):
    os.unlink(filenames)

archivex = zipfile.ZipFile('archivex.zip','a')
for folder,subfolders,filename_tuple in os.walk(path.cwd()):
    for files in filename_tuple:
        if files!='archivex.zip':
            archivex.write(files,compress_type=zipfile.ZIP_DEFLATED)
archivex.close()
i=input('press a key to continue reading what\'s been written')

archivex=zipfile.ZipFile('archivex.zip','r')
print(archivex.namelist())
archivex.close()

