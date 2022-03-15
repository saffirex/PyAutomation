import requests

result= requests.get('https://abhinasregmi.com.np/nicenice')

try:
    result.raise_for_status()
except Exception as exc:
    print(f'There was a problem: \n {exc}')
