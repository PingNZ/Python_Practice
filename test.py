# Coding:UTF-8


import requests

# url = 'http://www.6park.com'
# html = requests.get(url)
# html.encoding = "gb2312" # need to check the webpage's encode - charset
# print(html.text) 


url2 = 'http://www.skykiwi.com'
html2 = requests.get(url2)
print (html2.encoding)
print (html2.status_code)
# html2.encoding = "gbk"
# print(html2.text)


