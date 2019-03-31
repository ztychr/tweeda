import collections
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')


class WordSearch:

    # return amount of cursewords
    # searchword has to be a string
    @classmethod
    def search_word(self, List, searchword):
        amounts = 0
        newli = []

        for word in List:
            message = getattr(word, 'message')
            if message.__contains__(searchword):
                amounts = amounts + 1
                newli.append(message)
        return print("The word " + "'" + searchword + "'" + " appears " + str(amounts) + " times in the posts scraped \n")
        print(newli)

    @classmethod
    def word_counter(self, List):
        stopwords = ['the']
        for word in List:
            message = getattr(word, 'message')
        split_it = message.split()  # split() returns list of all the words in the string
        Counter = collections.Counter(split_it)  # Pass the split_it list to instance of Counter class.
        most_occur = Counter.most_common(10)

        print(most_occur)

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