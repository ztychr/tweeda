import requests
from bs4 import BeautifulSoup
import re
import time

urls = []

def crawl(url):

    html = requests.get("https://da.wikipedia.org/wiki/" + url)
    bs = BeautifulSoup(html.text, features="lxml")
    links = bs.find("div",{"id" : "bodyContent"}).find_all("a" , href=re.compile("(/wiki/)+([A-Za-z0-9_:()])+"))
    print("Response code: " + str(html.status_code))


    # Links per 1. side
    for link in links:
        title = link.get('title')
        href = link.get('href')

        if "/wiki/" in href:
            print (title)
            print (href)
            newurl = "https://da.wikipedia.org" + href
            urls.append(str(newurl))
        else:
            continue


        # Links per 2. side
        for item in urls:
            print(item)
            time.sleep(1)
            html2 = requests.get(item)
            bs2 = BeautifulSoup(html2.text, features="lxml")
            links = bs2.find("div",{"id" : "bodyContent"}).find_all("a" , href=re.compile("(/wiki/)+([A-Za-z0-9_:()])+"))

            for link in links:

                title = link.get('title')
                url = link.get('href')
                if "/wiki/" in url:
                    print ("-------> " + str(title) + str(url))
                    time.sleep(0.0005)
                else:
                    continue





searchstring = input("What would you like to search for? ")
crawl(searchstring)
