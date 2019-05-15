import unittest
from Post import tweet
from Scraping import Scraping
"""
Testing the 'tweet' class
"""

class test_tweet(unittest.TestCase):
    def setUp(self):
        self.aScrape = Scraping("realdonaldtrump", 2)


        self.aScrape.scrape_data()
        self.shortlist = self.aScrape.get_posts()



    def test_tweet(self):
        """
        Testing that scraping actually returns a 'Tweet' type
        """



        newTweet = self.shortlist[0]

        self.assertIsInstance(newTweet, tweet)

    def test_print_all(self):
        """
        Trying to a raise an error by putting non-tweet types into a list of tweets, and printing
        them all with this method, causing a 'AttributeError', and showing the downside to pythons dynamic ducktyping.
        More specificly, im trying to put at scraping-object into the list
        """

        dumbScrape = Scraping("realdonaldtrump", 1)

        self.shortlist.append(dumbScrape)
        self.assertRaises(AttributeError, tweet.print_tweetlist, self.shortlist)








