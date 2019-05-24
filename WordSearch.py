import collections
import nltk.corpus
from Statistical import statistical
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt', quiet=True)

"""
The WordSearch class searches the message attribute for a chosen word and returns how many times it appears
"""


class WordSearch:

    # returns amoint of posts with certain word
    # searchword has to be a string
    @classmethod
    def search_word(self, List, searchword):
        amounts = 0
        li = []
        for word in List:
            message = getattr(word, 'message')
            if message.__contains__(searchword):
                amounts = amounts + 1
        return amounts
    @classmethod
    def word_counter(self, List):
        allwords =[]

        stops = set(stopwords.words('english'))
        for word in List:
            tempfiltered = []
            message = getattr(word, 'message')
            split_it = message.split()  # split() returns list of all the words in the string
            for w in split_it:
                if not stops.__contains__(w):
                    tempfiltered.append(w)
            allwords.extend(tempfiltered)

        Counter = collections.Counter(allwords)  # Pass the split_it list to instance of Counter class.
        most_occur = Counter.most_common(5)


        return most_occur

    @classmethod
    def word_counter2(self, List):
        for word in List:
            message = getattr(word, 'message')

        en_stops = set(stopwords.words('english'))
        word_tokens = word_tokenize(message)

        filtered_sentence = [w for w in word_tokens if not w in en_stops]
        filtered_sentence = []

        for w in word_tokens:
            if w not in en_stops:
                filtered_sentence.append(w)
                Counter = collections.Counter(filtered_sentence)
                most_occur = Counter.most_common(5)
        print(word_tokens)
        print(most_occur)

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

