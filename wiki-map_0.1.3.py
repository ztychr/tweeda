#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import urllib.parse

r = requests.get('https://da.wikipedia.org/wiki/elefant')

bs = BeautifulSoup(r.text, features='lxml')

urls = []

#print(bs.prettify())

for i in bs.find_all('p'):

    for j in i.find_all('a'):

        li = j.get('href')
        urllib.parse.unquote(li)
        urls.append('https://da.wikipedia.org' + li)

        for x in urls:
            print(x)
