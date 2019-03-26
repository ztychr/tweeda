import Scraping
import statistical



newscrape = Scraping.Scraping("realdonaldtrump", 10)

Secondscrape = Scraping.Scraping("realdonaldtrump", 25)

newscrape.scrape_data()

allpost = newscrape.get_posts()


listofposts = newscrape.get_posts()
sortedList_likes = newscrape.bubble_sort('likes')
reversesort_replys = newscrape.bubble_sort_reverse('replys')

averagelikes = statistical.statistical.get_average(sortedList_likes, 'likes')
medianlikes = statistical.statistical.get_median(sortedList_likes, 'likes')

Reply_frequence = statistical.statistical.frequency_grouping(sortedList_likes, 'replys', 1000, 5000, 10000,20000, 50000)
print("average amount of likes: "+ str(averagelikes))
print("median likes: " + str(medianlikes))


deviation = statistical.statistical.standard_deviation(listofposts, 'likes')

native_deviation = statistical.statistical.native_sd(listofposts, 'likes')






#reversSortPost = newscrape.bubble_sort_reverse("likes")

#for i in bubblesort:
 #   print(i.print_all())

