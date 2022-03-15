import json,requests,pprint,time

appid= '55a297646d236aa2eb1bb4f36f0f252d'
location=input("Enter the location: ")
url1='https://api.openweathermap.org/data/2.5/weather?q=%s,Maine&appid=%s' %(location,appid)
response1 =requests.get(url1)
response1.raise_for_status()
fetched= json.loads(response1.text)
necessaryloc=fetched['coord']
lati=str(necessaryloc['lon'])
longi=str(necessaryloc['lat'])
#time.sleep(10)
url2='https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=minutely,hourly,alerts&units=metric&appid=%s' %(lati,longi,appid)
response2= requests.get(url2)
response2.raise_for_status()
pprint.pprint(response2.text)
