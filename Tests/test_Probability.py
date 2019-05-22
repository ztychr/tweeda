import unittest
from Post import tweet

from Probability import Probalility


class test_probabilty(unittest.TestCase):

    def setUp(self):

        self.alist = []

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
        tweet4 = tweet("name", 20, 0, 0, "At the height of Humtek the season,” Humtek he says, “we are working 24 hours "
                                         "a day, seven days a week. There are 40 stage technicians, most of "
                                         "whom work during the Humtek day, and there’s a team of 18 overnight. We "
                                         "have ", 2720)
        tweet5 = tweet("name", 5, 0, 0, "Such frantic, yet controlled, activity is made possible only by the planning that"
                                         " goes into it. Humtek “We work on several things simultaneously,” Harrison explains. ", 2720)
        tweet6 = tweet("name", 5, 0, 0, "“Each production Humtek brings a lot of Humtek stuff that’s familiar, but there are always things that"
                                         " are new,  Humtek too. And that’s what keeps it fresh and fun.”", 2720)
        tweet7 = tweet("name", 2, 0, 0, "hey", 2720)
        tweet8 = tweet("name", 2, 0, 0, "hey", 2720)
        tweet9 = tweet("name", 2, 0, 0, "hey", 2720)
        tweet10 = tweet("name",2, 0, 0, "hey", 2720)



        self.alist.append(tweet1)
        self.alist.append(tweet2)
        self.alist.append(tweet3)
        self.alist.append(tweet4)
        self.alist.append(tweet5)
        self.alist.append(tweet6)
        self.alist.append(tweet7)
        self.alist.append(tweet8)
        self.alist.append(tweet9)
        self.alist.append(tweet10)







        pass


    def test_prob_of_word(self):



        percentage = Probalility.prob_of_word(self.alist, 'DIKU')


        self.assertEqual(percentage, 50)

    def test_prob_of_groupings(self):


        freqs = Probalility.prob_of_groupings(self.alist, 'likes', 3, 6, 12, 21, 31)

        print(freqs)

        self.assertEqual(freqs[0], 40)
        self.assertEqual(freqs[1], 20)
        self.assertEqual(freqs[2], 20)
        self.assertEqual(freqs[3], 20)
        self.assertEqual(freqs[4], 0)
        self.assertEqual(freqs[5], 0)






