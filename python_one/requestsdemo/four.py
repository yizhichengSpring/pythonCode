import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
for key,values in r.cookies.items():
    print(key,values)