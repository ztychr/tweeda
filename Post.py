"""
The class of our tweet/post object. Is made so that we have a list of objects that we can manipulate
    with our sorting algorithms, without getting our lists ruined
"""


class tweet:


    def __init__(self, userName, likes, replys, retweets, message, ID):
        self.userName = userName
        self.likes = likes
        self.replys = replys
        self.retweets = retweets
        self.message = message
        self.reactions = likes + replys + retweets
        self.lenMessage = len(self.message)
        self.mentions = self.message.count('@')
        self.hastags = self.message.count('#')
        self.ID = ID

    def get_userName(self):
        return self.userName
    def get_likes(self):
        return self.likes
    def get_replys(self):
        return self.replys
    def get_retweets(self):
        return self.retweets
    def get_message(self):
        return self.message
    def get_lenmessage(self):
        return self.lenMessage
    def get_ID(self):
        return self.ID

    #simply a method to print all attribute of an object
    def print_all(self):
        print("username: " + self.userName)
        print("likes: " + str(self.likes))
        print("replys: " + str(self.replys))
        print("retweets: " + str(self.retweets))
        print("message: "+ self.message)
        print("length of message: " + str(self.lenMessage))
        print("ID number: " + str(self.ID))
        print("\n\n")
        return self.userName, self.likes,self.replys,self.retweets,self.message,self.lenMessage
