import os
from pathlib import Path as path

str=input("enter a string without spaces: ")

letters=[]
new_dir_path = path.cwd()
for x in str:
    new_dir_path= new_dir_path/ x #first iter: adds x to cwd, second iter adds x to previous path

os.makedirs(new_dir_path) #makes new directory
os.chdir(new_dir_path)

#makedirs creates all intermediatory paths as 
# if str= 'safal':
#new_dir_path=cwd/s --> cwd/s/a ----> cwd/s/a/f/a/l while directories aren't created yet
#then makedirs makes all dirs

#whereas
print(path.cwd())
str2=input("enter a string without spaces: ")
new_dir_path2 = path.cwd() #initialize path obj
for x in str2:
    new_dir_path2= new_dir_path2 / x
    new_dir_path2.mkdir() #calling mkdir on path object

    




