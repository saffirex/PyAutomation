file= open('purey2.txt','r')
newlines=[]
def adder(line):
    string= '"'+line.partition("\n")[0]+r'\n"'+"\n"
    return string
for line in file.readlines():
    newlines.append(adder(line))
file.close
file2= open("newfile.txt",'w')
print(newlines)
file2.writelines(newlines)