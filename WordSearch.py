import profanity


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