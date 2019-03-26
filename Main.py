import Scraping
from Statistical import *


tHandle = input("Enter twitter handle: ")
postamountsInput = input("Enter amount of tweets:  ")
postamountsInt = int(postamountsInput)

ourScrape = Scraping.Scraping(tHandle, postamountsInt)


#reversSortPost = newscrape.bubble_sort_reverse("likes")

#for i in bubblesort:
 #   print(i.print_all())
