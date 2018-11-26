import urllib.request
from bs4 import BeautifulSoup

url = "https://www.bloomberg.com/quote/SPX:IND%27"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
soup = BeautifulSoup(response, "html.parser")
# print (response.read().decode('utf-8'))
print(soup)
print("hey")