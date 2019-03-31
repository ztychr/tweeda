from collections import Counter


class WordSearch:

    # return amount of cursewords
    # searchword has to be a string
    @classmethod
    def search_word(self, List, searchword):
        amounts = 0

        for word in List:
            message = getattr(word, 'message')
            if message.__contains__(searchword):
                amounts = amounts + 1
        return print("The word " + "'" + searchword + "'" + " appears " + str(amounts) + " times in the posts scraped")

    @classmethod
    def word_counter(self, List, words_to_count):
        for word in List:
            message = getattr(word, 'message')
        split_it = message.split()  # split() returns list of all the words in the string
        #Counter = Counter(split_it)  # Pass the split_it list to instance of Counter class.
        most_occur = Counter.most_common(4)

        print(most_occur)
