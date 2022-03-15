import requests, bs4

res=requests.get('https://nostarch.com')
res.raise_for_status()
#remember to pass a file object and not a filename
examplefile= open('E:\Python\webscraping\example.html')
nostarchsoup = bs4.BeautifulSoup(examplefile,'html.parser')
#pass the file object and then the parser to use for parsing the file
elems=nostarchsoup.select('#author')
print(type(elems))
print(elems)
