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

    # return amount of cursewords
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
        for word in List:
            message = getattr(word, 'message')
            split_it = message.split()  # split() returns list of all the words in the string
            allwords.extend(split_it)



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
    def word_correlation(self, List, attr, searchWord):
        # Returns the average like of all posts
        # and returns the average likes of the posts with the search word
        li = []
        avg_attr = statistical.get_average(List, attr)
        print(avg_attr , "Avg likes of all posts")

        for posts in List:
            message = getattr(posts, 'message')
            if message.__contains__(searchWord):
                li.append(posts)

        newAvg_attr = statistical.get_average(li, attr)

        if (newAvg_attr > avg_attr):
            differenceInAttr = newAvg_attr-avg_attr
            new = int(differenceInAttr)
            print('Posts containing the word ' + "'" + searchWord + "'" + " has in average " + str(new) + " more " + attr)
            print("")

            return li

        if(newAvg_attr < avg_attr):
            differenceInAttr2 = avg_attr-newAvg_attr
            new2 = int(differenceInAttr2)
            print('Posts containing the word ' + "'" + searchWord + "'" + " has on average " + str(new2) + " less " + attr)
            print("")

            return li
