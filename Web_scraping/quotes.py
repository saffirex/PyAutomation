import requests
from bs4 import BeautifulSoup as bsoup

website= requests.get('https://quotes.toscrape.com/')

soup= bsoup(website.text, 'html.parser')
#finding the title by tag
title= soup.find('title')
print(title.text)

#finding the first link
link= soup.find('a')
#print(link.text)
#finding by css class
quote= soup.find(class_='text') #class_ to not conflict with the reserved keyword class in Python
#print(quote.text)

#finding all the links in the website
all_links=soup.find_all('a') #notice the underscore
#print(all_links) #cannot use .text method on a list

for each in all_links:
    text_form=each.text #we find the text from each element in the list 'all_links'
    #print(text_form)

quotes=soup.find_all(class_='text')
for each in quotes:
    print(each.text)
