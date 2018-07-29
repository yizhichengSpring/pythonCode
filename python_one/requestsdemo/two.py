import requests


#参数
data = {'name':'yzc','age':22}

r = requests.get('http://httpbin.org/get',params=data)
print(r.text)
print(r.json())
print(type(r.json()))