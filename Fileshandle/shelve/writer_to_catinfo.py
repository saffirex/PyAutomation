import pprint as pp
cats= [{'name': 'tom', 'colour':'blue', 'cartoon':'tom&jerry'},{'name':'felix','colour':'idk','cartoon':'felix the cat'}]
fileobj= open('catinfo.py','w') #the mode in which you open the file decides whether a new file will be created or the text will be appended on the existing file
fileobj.write('cats=' + pp.pformat(cats)+ '\n\n\n')
fileobj.close()