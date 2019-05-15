import unittest
from Scraping import Scraping

"""
Testing the 'Scraping' class
"""

class testScraping(unittest.TestCase):

    def test_Scraping(self):
        """
        Testing the 'Scraping' constructor
        """
        print("testing Scraping construct")

        aScrape = Scraping("realdonaldtrump", 2)
        self.assertEqual(aScrape.r.url, "https://twitter.com/realdonaldtrump")
        self.assertEqual(aScrape.r.status_code, 200)

    def test_scrape_data(self):
        aScrape = Scraping("realdonaldtrump", 2)

        aScrape.scrape_data()
        print(type(aScrape.find_tweets[0]))

        self.assertGreater(len(aScrape.find_tweets),0)

    def test_get_posts(self):
        """
        Trying to fill the wrong types of objects into 
        """

        
        aScrape = Scraping("realdonaldtrump", 2)


        aScrape.scrape_data()

        listofposts = aScrape.get_posts()

        self.assertTrue(listofposts)


