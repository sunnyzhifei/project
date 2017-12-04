import urllib.request as re

response = re.urlopen("http://www.baidu.com")
x=response.read()
print(x)