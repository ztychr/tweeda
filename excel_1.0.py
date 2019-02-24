from bs4 import BeautifulSoup
import requests
import urllib.parse
import xlsxwriter

def crawl():

    while True:
        #excelrows
        row = 0
        col = 0
        rawinput = input('Enter your searchstring: ')
        searchstring = rawinput.replace(" ", "_")

        workbook = xlsxwriter.Workbook(rawinput + ".xlsx")# laver et exceldoc
        worksheet = workbook.add_worksheet("My sheet") # laver siden på exceldoccet som vi vil arbejde på

        r = requests.get('https://wikipedia.org/wiki/' + searchstring) # hent url med en webhandler

        bs = BeautifulSoup(r.text, features='lxml') # lav

        titles = [] # laver tom liste
        urls = [] # laver tom liste
        worksheet.write(row, col, rawinput)
        worksheet.write(row, col+1, r.url)


        for i in bs.find_all('p'): # find alle <p> tags på en wikipedia-side
            for j in i.find_all('a'): # find alle <a> tags i <p> tags
                li = j.get('href') # find href værdien i alle <a> tags

                title = j.get('title') # laver en variable der fetcher titlen på linket
                links = 'https://wikipedia.org' + li # laver en variable der indeholder det fulde link

                if j.get('title') != None and j.get('href') != None: # sorterer alle links som ikke har en titel fra
                    urls.append(links)
                    titles.append(title)
                    worksheet.write(row, col+2, title)
                    worksheet.write(row, col+ 3, links)
                    row = row +1;

        print("root url: " + r.url)
        print('URL\'s  :  ' + str((len(urls)))) # print længde af liste
        print('Titles :  ' + str((len(titles))) + '\n') # print længde af liste

        # tester om der kan scrapes noget fra url.
        if not titles and not urls:
            print('No articles were found.')
            continue
        else:
            break

    # prints title, url...
    for x, y in zip(titles, urls):
        urllib.parse.quote_plus(x, y)
        print(x + ' :', y)

    workbook.close()

crawl()