import copy as cp
name= "the quick brown fox jumps over the lazy dog"
print(name[4:9])

name2= name[0:4]+ 'prick' + name[9:len(name)]
print(name2)

name2= cp.deepcopy(name)
print(name2)