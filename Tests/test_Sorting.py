
import unittest
from Post import tweet
from Scraping import Scraping
from Sorting import Sorting
from Organizer import Organizer
import random
"""
Testing the 'sorting' class.
this testclass is mostly testing for the execution speed of both the 'bubblesort and 'Quicksort algoritm, using
a list with randomly generated 'likes'-values of a 100 elements. the values are between 0-100 
"""

class test_Sorting(unittest.TestCase):
    
    def setUp(self):
        """
        Creating the list of 'dumb' post-objects that can be sorted on by both algorithms for comparison
        """
        self.postList = []
        for i in range(0,21000):
            num = random.randint(0,100)
            tempPost = tweet("tempPost", num, 0, 0, "somemessage", "1337")
            self.postList.append(tempPost)

        """
        Also creating a very short list, for checking how tthe sorting works out
        """
        self.shortlist = []
        post_four = tweet("apost", 3, 0, 0, "first2", "256")
        post_one = tweet("apost", 4, 0,0, "somemesage", "256")
        post_two = tweet("apost", 5, 0, 0, "somemesage", "256")
        post_three = tweet("apost", 2, 0, 0, "somemesage", "256")
        post_six = tweet("apost", 0, 0, 0, "somemesage", "256")
        post_five = tweet("apost", 3, 0, 0, "second2", "256")
        post_seven = tweet("apost", 15, 0, 0, "somemesage", "256")

        self.shortlist.append(post_one)
        self.shortlist.append(post_two)
        self.shortlist.append(post_three)
        self.shortlist.append(post_four)
        self.shortlist.append(post_five)
        self.shortlist.append(post_six)
        self.shortlist.append(post_seven)

    def test_bubble_sort(self):
        """
        Testing speed for 'bubblesort'
        """
        print("Bubblesort")

        Sorting.bubble_sort(self.postList, 'likes')





        print("Bubblesort test done")

    def test_quick_sort(self):
        """
        Testing speed for 'Quicksort'
        """
        print("Quicsort")


        lenlist = len(self.postList)
        Sorting.quick_sort(self.postList, 0, lenlist-1, 'likes')




        print("Quicksort test done")
    def test_bubble_sort1(self):
        """
        Testing functionality  for 'Bubblesort'
        Also testing stability of 'bubblesort'
        """
        SortedList = Sorting.bubble_sort(self.shortlist, 'likes')

        tweet.print_tweetlist(SortedList)

        self.assertEqual(SortedList[0].get_likes(), 0)

        self.assertEqual(SortedList[1].get_likes(), 1)

        self.assertEqual(SortedList[2].get_likes(), 2)
        self.assertEqual(SortedList[3].get_likes(), 2)
        #testing stability:
        self.assertEqual(SortedList[2].get_message(), "first2")
        self.assertEqual(SortedList[3].get_message(), "second2")

        self.assertEqual(SortedList[4].get_likes(), 3)
        self.assertEqual(SortedList[5].get_likes(), 4)
        self.assertEqual(SortedList[6].get_likes(), 15)

    def test_quick_sort1(self):
        """
        Testing functionality  for 'Quicksort'

        """

        lenoflist = len(self.shortlist)
        Sorting.quick_sort(self.shortlist, 0, lenoflist-1, 'likes')

        tweet.print_tweetlist(self.shortlist)

        self.assertEqual(self.shortlist[0].get_likes(), 0)
        self.assertEqual(self.shortlist[1].get_likes(), 1)
        self.assertEqual(self.shortlist[2].get_likes(), 2)
        self.assertEqual(self.shortlist[3].get_likes(), 2)
        self.assertEqual(self.shortlist[2].get_message(), "first2")
        self.assertEqual(self.shortlist[3].get_message(), "second2")
        self.assertEqual(self.shortlist[4].get_likes(), 3)
        self.assertEqual(self.shortlist[5].get_likes(), 4)
        self.assertEqual(self.shortlist[6].get_likes(), 15)






















        
        