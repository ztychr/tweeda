import Scraping
import statistical

newscrape = Scraping.Scraping("realdonaldtrump", 24)

newscrape.scrape_data()

postlist = newscrape.get_posts()

onepost = postlist[0]

likes = onepost.get_likes()
likesplusone = statistical.statistical.plusone(onepost.get_likes())


#print(get.getObjectlist_len());

