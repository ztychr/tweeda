from bs4 import BeautifulSoup
import requests

import urllib.parse

r = requests.get('https://da.wikipedia.org/wiki/elefant')

bs = BeautifulSoup(r.text, features='lxml')

urls = []
titles = []


for i in bs.find_all('p'):
    for j in i.find_all('a'):
        li = j.get('href')
        title = j.get('title')
        links = "https://da.wikipedia.org/wiki" + li
        if (j.get('title') != None): # sorterer alle links som ikke har en titel fra
            urls.append(links)
        if j.get('title')!= None :
            titles.append(title)

len_urls = len(urls)
len_titles = len(titles)
print(len_urls)
print(len_titles)


print(urls)
print(titles)
