import urllib.request
response = urllib.request.urlopen('http://stackoverflow.com/')
html = response.read()
print(html)