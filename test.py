# Coding:UTF-8


import requests

url = 'http://www.6park.com'
html = requests.get(url)
html.encoding = "gb2312" # need to check the webpage's encode - charset
print(html.text)


