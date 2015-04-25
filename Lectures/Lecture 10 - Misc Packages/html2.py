import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://stackoverflow.com/')
html = response.read()
soup = BeautifulSoup(html)

print(soup.title)
print(soup.title.string)
print(soup.div)
