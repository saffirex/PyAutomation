import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(len(res.text))
if res.status_code == requests.codes.ok:
    print("the text can be received")
else:
    print("unable to access the page")