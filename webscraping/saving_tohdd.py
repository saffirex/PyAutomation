import requests
res=requests.get('https://abhinasregmi.com.np')
res.raise_for_status()
playfile= open('site.html', 'wb')
for chunk in res.iter_content(10000): # res.iter_content returns chunks of the content on each iteration of size specified as the argument
    playfile.write(chunk)
playfile.close()