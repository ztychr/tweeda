from bs4 import BeautifulSoup
import requests
import urllib.parse

r = requests.get('https://da.wikipedia.org/wiki/elefant')

bs = BeautifulSoup(r.text, features='lxml')

urls = []

#print(bs.prettify())

for i in bs.find_all('p'):
    for j in i.find_all('a'):
        li = print(j.get('href'))
        urls.append(li)
