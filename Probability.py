from Statistical import statistical
from WordSearch import WordSearch


class Probalility(statistical, WordSearch):
    """
    @:param list. lsit of tweets
    @:param word. a certain word
    :returns the percentage of posts that contains this word, result if rounded of
    """


    @classmethod
    def prob_of_word(cls,list ,word):

        samplesize = cls.search_word(list, word)
        fullsize = len(list)
        decimal = samplesize / fullsize
        percent = decimal * 100
        percentint = int(percent)
        return percentint

    """
    the same method as frequency_groupings() in statistical. it only returns percentages instead of numbers.
    """

    @classmethod
    def prob_of_groupings(cls,list, attrs, grouping1, grouping2, grouping3, grouping4=None, grouping5=None):

        fullsize = len(list)


        freqs =cls.frequency_grouping(list, attrs, grouping1, grouping2, grouping3, grouping4, grouping5)
        percents = []
        freqlen = len(freqs)

        for i in range(0, freqlen):
            tempdec = freqs[i] / fullsize
            percent = tempdec * 100
            percent = int(percent)

            percents.append(percent)

        return percents[0], percents[1], percents[2], percents[3], percents[4], percents[5]



