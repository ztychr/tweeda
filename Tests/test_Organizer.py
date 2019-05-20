import unittest
from Post import tweet
from Organizer import Organizer
import os
from Statistical import statistical
from Sorting import Sorting
from Scraping import Scraping
"""
Testing the 'Organizer' class. trying to create a document and then verifrying that it exists
"""

class test_statistical(unittest.TestCase):
    """
    Testing wihout doing any scraping. Using the faux twitterhandle 'mickeyMouse'
    """
    def setUp(self):
        self.handle = "mickeyMouse"
        self.payload = []
        tweet1 = tweet("name", 10, 0, 0, "text", 2720)
        tweet2 = tweet("name", 10, 0, 0, "text", 2720)
        tweet3 = tweet("name", 10, 0, 0, "text", 2720)
        tweet4 = tweet("name", 15, 0, 0, "text", 2720)
        tweet5 = tweet("name", 15, 0, 0, "text", 2720)
        tweet6 = tweet("name", 20, 0, 0, "text", 2720)
        tweet7 = tweet("name", 20, 0, 0, "text", 2720)

        self.payload.append(tweet1)
        self.payload.append(tweet2)
        self.payload.append(tweet3)
        self.payload.append(tweet4)
        self.payload.append(tweet5)
        self.payload.append(tweet6)
        self.payload.append(tweet7)

    def test_create_project(self):
        """
        Testing whether a path to a folder is generated
        since these tests are in another file, the generated file will appear in this directory
        """

        Organizer.create_project(self.handle)

        supposedpath = os.getcwd() + "/Jsondata_files"

        folderpath = os.listdir(supposedpath)

        self.assertGreater(len(folderpath), 0)
    def test_getpostList_Json(self):


        """
        Testing that, when reading from a generated file, it is possible to get python-postpbjects
        from it.
        it is a little dumb, but you have to provide console input to run test
        """
        newScrape = Scraping("BarackObama", 3)

        newScrape.scrape_data()

        payload = newScrape.get_posts()

        Organizer.create_project("BarackObama")

        Organizer.write_file_json(payload, "BarackObama")

        supposedpath = os.getcwd() + "/Jsondata_files/BarackObama"

        list , path = Organizer.getpostList_Json()


        self.assertIsInstance(list[0], tweet)
        self.assertEqual(path, supposedpath)









        #self.assertTrue(os.path.isfile(supposedpath))

