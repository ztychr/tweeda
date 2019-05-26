import unittest
from WordSearch import WordSearch
from Statistical import statistical
from Post import tweet

"""
Testing 'WordSearch'
"""

class test_WordSearch(unittest.TestCase):

    def setUp(self):
        self.alist = []
        """
        the list that we are testing on the word 'humtek' has been added many times as the most commen word.
        The word 'is' has been added many times as well, but that should be sorted away
        The word 'DIKU' is used to check word_correlation
        """
        tweet1 = tweet("name", 10, 0, 0, "Production Humtek is manager Tom Harrison,  DIKU"
                                         "who has been Humtek is working at Glyndebourne DIKU "
                                         "for 20 years, Humtek believes that this unique DIKU "
                                         "quality Humtek is wh Humtek at keeps people coming back.DIKU "
                                         "“This is a very different is operation to the on", 2720)
        tweet2 = tweet("name", 10, 0, 0, "that started in 1934,” DIKU he is says, “but there’s still the"
                                         " notion Humtek  that you are here at the invitation of the Christie "
                                         "family. Plus there’s  Humtek is the sense of occasion, the opportunity to "
                                         "appreciate the gardens. People is come at 3pm and make a day of it.”", 2720)
        tweet3 = tweet("name", 20, 0, 0, "It’s  DIKU Harrison’s Humtek job to help make sure that each day is crowned by "
                                         "a perfect performance, and his calm demeanour belies the sheer "
                                         "amount of work that goes into creating Glyndebourne, all year round.", 2720)
        tweet4 = tweet("name", 20, 0, 0, "At the DIKU height of Humtek the season,” Humtek he says, “we are working 24 hours "
                                         "a day, seven days a week. There are 40 stage technicians, most of "
                                         "whom work during the Humtek day, and there’s a team of 18 overnight. We "
                                         "have ", 2720)
        tweet5 = tweet("name", 5, 0, 0, "Such frantic, yet controlled, activity is made possible only by the planning that"
                                         " goes into it. Humtek “We work on several things simultaneously,” Harrison explains. ", 2720)
        tweet6 = tweet("name", 5, 0, 0, "“Each production Humtek brings a lot of Humtek stuff that’s familiar, but there are always things that"
                                         " are new,  Humtek too. And that’s what keeps it fresh and fun.”", 2720)
        tweet7 = tweet("name", 10, 0, 0, "To these ears,  Humtek Harrison’s working week sounds exhausting. But each to his own. “I’ve been"
                                         " on stage with Il barbiere Humtek di Siviglia (The Barber of Seville) this ", 2720)

        self.alist.append(tweet1)
        self.alist.append(tweet2)
        self.alist.append(tweet3)
        self.alist.append(tweet4)
        self.alist.append(tweet5)
        self.alist.append(tweet6)
        self.alist.append(tweet7)

    def test_search_word(self):
        print(self.alist)

        """
        the word humtek appears in  all posts, so this method should be returning 7
        """

        occurences = WordSearch.search_word(self.alist, 'Humtek')

        self.assertEqual(occurences, 7)

    def test_word_counter(self):

        most_common = WordSearch.word_counter(self.alist)
        self.assertEqual(most_common[0][0], 'Humtek')
        self.assertIsNot(most_common[1], 'is')



    def test_word_correlation(self):
        """
        the dataset is made in such a way that the elements with 'DIKU' should have a greater average
        """
        DIKU = WordSearch.word_correlation(self.alist,'DIKU')

        #the average of the whole list should be greater than average of the elements containing 'DIKU'
        self.assertGreater(statistical.get_average(self.alist, 'reactions'), DIKU)

