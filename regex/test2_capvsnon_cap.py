import re
s = r'abc123d, hello 3.1415926, this is my book'
pattern = r'-?[0-9]+(\.[0-9]*)?|-?\\.[0-9]+'
m = re.search(pattern, s).group() #can do group(1)
n= re.search(pattern, s).groups()
o= re.findall(pattern, s)
print(m)
print(n)
print(o)
#vs non-capturing
print("===========================")
pattern2 = r'-?[0-9]+(?:\\.[0-9]*)?|-?\\.[0-9]+'
m = re.search(pattern2, s).group() #cannot do group(1)
n= re.search(pattern2, s).groups()
o= re.findall(pattern2, s)
print(m)
print(n)
print(o)