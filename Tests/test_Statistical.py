
from Post import tweet
from Statistical import statistical
from Sorting import Sorting
from Scraping import Scraping
"""
Testing the 'tweet' class
"""
import unittest

class test_statistical(unittest.TestCase):

    def setUp(self):
        self.alist = []
        tweet1 = tweet("name", 10, 0, 0, "text", 2720)
        tweet2 = tweet("name", 10, 0, 0, "text", 2720)
        tweet3 = tweet("name", 10, 0, 0, "text", 2720)
        tweet4 = tweet("name", 15, 0, 0, "text", 2720)
        tweet5 = tweet("name", 15, 0, 0, "text", 2720)
        tweet6 = tweet("name", 20, 0, 0, "text", 2720)
        tweet7 = tweet("name", 20, 0, 0, "text", 2720)

        self.alist.append(tweet1)
        self.alist.append(tweet2)
        self.alist.append(tweet3)
        self.alist.append(tweet4)
        self.alist.append(tweet5)
        self.alist.append(tweet6)
        self.alist.append(tweet7)


    def test_get_average(self):
        testAverage = statistical.get_average(self.alist, 'likes')

        self.assertEqual(testAverage, 14)

    def test_get_median(self):

        lenlist = len(self.alist)
        # necessary to sort the list first on the relevant attribute

        Sorting.quick_sort(self.alist, 0 , lenlist-1, 'likes')

        median = statistical.get_median(self.alist, 'likes')

        self.assertEqual(median, 15)


    def test_frequency_grouping(self):
        # testing with, and without the overloaded arguments:
        freq = statistical.frequency_grouping(self.alist, 'likes', 12, 16, 21)

        self.assertEqual(freq[0], 3)
        self.assertEqual(freq[1], 2)
        self.assertEqual(freq[2], 2)
        self.assertEqual(freq[3], 0)

        # adding some more stuff to the list, and then testing with all arguments used

        self.alist.append(tweet("name", 30, 0, 0, "text", 2720))
        self.alist.append(tweet("name", 100, 0, 0, "text", 2720))

        freq1 = statistical.frequency_grouping(self.alist, 'likes',12, 16 ,21, 31, 101)
        self.assertEqual(freq1[0], 3)
        self.assertEqual(freq1[1], 2)
        self.assertEqual(freq1[2], 2)
        self.assertEqual(freq1[3], 1)
        self.assertEqual(freq1[4], 1)
        self.assertEqual(freq1[5], 0)


    def test_standard_deviation(self):

        sd = statistical.standard_deviation(self.alist, 'likes')
        self.assertEqual(sd, 4.17)

