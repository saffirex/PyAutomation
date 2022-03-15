from bs4 import BeautifulSoup as bsoup
import requests
import random
site_html= requests.get('https://www.goodreads.com/quotes') #this doesn't give the html but gives the request object

soup=bsoup(site_html.text, 'html.parser')

for each in soup.find_all(class_='quoteText'):
    print(each.text)