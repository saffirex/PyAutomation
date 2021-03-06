from bs4 import BeautifulSoup as bsoup
import requests

page_num=1
next_button=True

while next_button:
    print("="*10+" "+str(page_num)+" "+"="*10)
    print("="*25)
    site_html= requests.get('https://www.goodreads.com/quotes?page='+str(page_num)) #this doesn't give the html but gives the request object
    soup=bsoup(site_html.text, 'html.parser')
    for each in soup.find_all(class_='quoteText'):
        print(each.text.split('\n')[1],each.text.split('\n')[4], end='\n\n')
        print("...........................................")
    next_button= soup.select_one('a.next_page')
    page_num+=1