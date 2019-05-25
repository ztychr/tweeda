import collections
import nltk.corpus
from Statistical import statistical
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt', quiet=True)

"""
The WordSearch has a collection of methods that search for specific words, and return some information
"""


class WordSearch:
    """
    @:param List: list of tweet-objects
    @:param searchword: the word that is to be searched for
    @:returns The amount of times that the given word appears in the given list
    """
    @classmethod

    def search_word(self, List, searchword):
        amounts = 0
        li = []
        for word in List:
            message = getattr(word, 'message')
            if message.__contains__(searchword):
                amounts = amounts + 1
        return amounts
    """
    @:param List: list of tweet-objects
    @:returns a tuple of the five most common words. Common words are left out
    """
    @classmethod
    def word_counter(self, List):
        allwords =[]
        # 'stops' indeholder alle almindelige ord,
        # som f.eks. "is" og "and", dem vil vi ikke tælle
        stops = set(stopwords.words('english'))

        #Gennemløb af alle 'messages' i posts.
        for word in List:
            tempfiltered = []
            message = getattr(word, 'message')
            split_it = message.split()
            # Hver message i listen bliver lavet om
            # til en liste af ord som kan tilføjes til
            #en større liste af ord
            for w in split_it:
                if not stops.__contains__(w):
                    tempfiltered.append(w)
            allwords.extend(tempfiltered)

        #funktionen most_common() kan bruges til at finde
        #de strings der fremgår flest gange
        Counter = collections.Counter(allwords)
        most_occur = Counter.most_common(5)


        return most_occur

    """
    @:param List: list of tweet-objects
    @:param searchword: the word that is to be searched for
    @:returns the amount of total reactions more or less that posts containing this word is expected to have
    """

    @classmethod
    def word_correlation(self, List, searchWord):
        # Returns the average like of all posts
        # and returns the average likes of the posts with the search word
        li = []
        avg_attr = statistical.get_average(List, 'reactions')


        for posts in List:
            message = getattr(posts, 'message')
            if message.__contains__(searchWord):
                li.append(posts)

        if len(li) != 0:
            newAvg_attr = statistical.get_average(li, 'reactions')


            differenceInAttr = newAvg_attr-avg_attr
            new = int(differenceInAttr)


            return new
        else:
            return 0

