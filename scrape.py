import urllib.request
from bs4 import BeautifulSoup

url = "https://www.pythonforbeginners.com"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
soup = BeautifulSoup(response, "html.parser")
# print (response.read().decode('utf-8'))
# print(soup)

tags = soup.findAll("div", class_="post-bodycopy cf")
# tags = soup.findAll("h2")

print(tags[0].string)





