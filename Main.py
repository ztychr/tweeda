from Organizer import Organizer
from Scraping import Scraping

twitterhandle = input("\nEnter account to scrape: ")
tweetamount = input("Enter amount of tweets: ")
tweetamountInt = int(tweetamount)
print(" ")

newscrape = Scraping(twitterhandle, tweetamountInt) # Object of the user name and amounts of tweets to be scraped
newscrape.scrape_data() # Scarping object
allpost = newscrape.get_posts() # Returns list of posts

"""
Iterating through all attributes
and returning each
"""
#for u in allpost:
 #   u.print_all()

"""
Quick_sort returns a sorted list on attribute high to low
"""
#lenlist = len(allpost)
#Sorting.quick_sort(allpost, 0, lenlist, 'likes')

#for i in allpost:
 #   i.print_all()

#for posts in sortedList_likes:
#posts. print_all()

"""
Reversesort_replys is returning the sorted list reversed 
"""
#reversesort_replys = newscrape.bubble_sort_reverse('replys')

"""
Averagelikes returns the average of Eg. 'likes
"""
#averagelikes = statistical.get_average(sortedList_likes, 'likes')

"""
Medianlikes returns the the median of a sorted list
"""
#medianlikes = statistical.get_median(sortedList_likes, 'likes')

"""
Reply_frequence returns the frequency of chosen groupings
"""
#Reply_frequence = statistical.frequency_grouping(sortedList_likes, 'replys', 1000, 5000, 10000,20000, 50000)

"""
Deviation returns the deviation of a chosen attribute
"""
#deviation = statistical.standard_deviation(allpost, 'likes')

"""
WordSearch searches how many time a word appears in the scraped list
"""
#WordSearch.search_word(sortedList_likes, "Mexico")
#WordSearch.word_counter(sortedList_likes)
#WordSearch.word_counter2(sortedList_likes)

#listOfwords = WordSearch.word_correlation(sortedList_likes, 'likes', 'Citizenship')
#for searchWord in listOfwords:
    #searchWord.print_all()

"""
Creates a project directory and writes data to a Json file
"""
Organizer.create_project(twitterhandle)
Organizer.write_file_json(allpost, twitterhandle)

