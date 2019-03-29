from Scraping import Scraping
from Statistical import statistical


# Først laver initialiserer man objektet:
newscrape = Scraping("realdonaldtrump", 10)

# Så kører man metoden scrape_data(), på sit objekt, så er scrapingen blevet udført:
newscrape.scrape_data()

# Og når man kalder get_posts, kan man få returneret en liste af posts:
allpost = newscrape.get_posts()

# Hvis man gerne vil have printet alle attibutter på alle objekter i listen, skal man bruge et forloop, til at gå igennem listen:


#Hvis jeg gerne vil have sorteret listen fra høj-lav, på attributen 'likes' gør jeg således:
sortedList_likes = newscrape.bubble_sort('likes')
for posts in sortedList_likes:
    posts. print_all()

#Hvis jeg gerne vil sortere den anden vej rundt kalder jeg i stedet bubble_sort_reverse()
# I det her tilfælde sorterer jeg bare på 'replys'
reversesort_replys = newscrape.bubble_sort_reverse('replys')

#Hvis jeg vil have gennemsnittet af f.eks. likes i listen gør jeg dette. 
averagelikes = statistical.get_average(sortedList_likes, 'likes')

#Hvis jeg vil have medianen gør jeg det her:
#Listen skal være sortet når man skal have medianen, eller giver det ingen mening
medianlikes = statistical.get_median(sortedList_likes, 'likes')


# Den her metode er måske lidt mere tricky.
#Her får man frekvensen af forskellige mænngder af ting indenfor forskellige grupperinger
# kan evt bruges til at lave et pindediagram
Reply_frequence = statistical.frequency_grouping(sortedList_likes, 'replys', 1000, 5000, 10000,20000, 50000)


# Standardafvigelse af en bestemt attribut. 
deviation = statistical.standard_deviation(allpost, 'likes')