import profanity


class Profanity:


  # return amount of cursewords
  # searchword has to be a string
    @classmethod
    def search_word(self, List, searchword):
        amounts = 0

        for word in List:
            message = getattr(word, 'message')
            if message.__contains__(searchword):
                amounts = amounts + 1
        return print("all the posts have the word: " + searchword + " " + str(amounts) + " times" )