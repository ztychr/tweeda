import requests
from bs4 import BeautifulSoup
import re

urls = []

def crawl(url):

    html = requests.get("https://da.wikipedia.org/wiki/" + url)

    bs = BeautifulSoup(html.text, features="lxml")
    links = bs.find("div",{"id" : "bodyContent"}).find_all("a" , href=re.compile("(/wiki/)+([A-Za-z0-9_:()])+"))

    print("Response code: " + str(html.status_code))

    for link in links:
        title = link.get('title')
        href = link.get('href')
        print (title)
        newurl = "https://da.wikipedia.org" + href
        urls.append(str(newurl))

        for item in urls:
            #print(item)
            html2 = requests.get(item)
            bs2 = BeautifulSoup(html2.text, features="lxml")
            links = bs2.find("div",{"id" : "bodyContent"}).find_all("a" , href=re.compile("(/wiki/)+([A-Za-z0-9_:()])+"))

            for link in links:
                title = link.get('title')
                href = link.get('href')
                print (title)
                newurl = "https://da.wikipedia.org" + href



searchstring = input("What would you like to search for? ")
crawl(searchstring)
