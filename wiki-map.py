import requests
from bs4 import BeautifulSoup
import re


def crawl(url):

    html = requests.get("https://da.wikipedia.org/wiki/" + url)
    bs = BeautifulSoup(html.text, features="lxml")
    links = bs.find("div",{"id" : "bodyContent"}).find_all("a" , href=re.compile("(/wiki/)+([A-Za-z0-9_:()])+"))

    print("Response code: " + str(html.status_code))

    for link in links:
        title = link.get('title')
        href = link.get('href')
        print (title)
        newurl = print ("https://da.wikipedia.org/wiki/" + href + "\n")

searchstring = input("What would you like to search for? ")
crawl(searchstring)
