from bs4 import BeautifulSoup
import requests
import urllib.parse

def crawl():

    rawinput = input('Enter your searchstring: ')

    searchstring = rawinput.replace(" ", "_")
    r = requests.get('https://wikipedia.org/wiki/' + searchstring) # hent url med en webhandler

    bs = BeautifulSoup(r.text, features='lxml') # lav

    titles = [] # laver tom liste
    urls = [] # laver tom liste

    for i in bs.find_all('p'): # find alle <p> tags på en wikipedia-side
        for j in i.find_all('a'): # find alle <a> tags i <p> tags
            href = j.get('href') # find href værdien i alle <a> tags
            li = href.replace(" ", "_")

            title = j.get('title') # laver en variable der fetcher titlen på linket
            links = 'https://wikipedia.org' + li # laver en variable der indeholder det fulde link

            if j.get('title') != None and j.get('href') != None: # sorterer alle links som ikke har en titel fra
                urls.append(links)
                titles.append(title)


    print("root url: " + r.url)
    print('URL\'s  :  ' + str((len(urls)))) # print længde af liste
    print('Titles :  ' + str((len(titles))) + '\n') # print længde af liste

    # print -->
    # titles[1], urls[1],
    # tiles[2], urls[2]
    # ...
    for x, y in zip(titles, urls):
        urllib.parse.quote_plus(x, y)
        print(x + ' :', y)


crawl()
