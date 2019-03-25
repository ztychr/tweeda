class tweet:



    def __init__(self, userName, likes, replys, retweets, message):
        self.username = userName
        self.likes = likes
        self.replys = replys
        self.retweets = retweets
        self.message = message
        self.lenMessage = len(self.message)
        self.mentions = self.message.count('@')
        self.hastags = self.message.count('#')

    def get_userName(self):
        return self.username
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

    def print_all(self):
        print("username: " + self.username)
        print("likes: " + str(self.likes))
        print("replys: " + str(self.replys))
        print("retweets: " + str(self.retweets))
        print("message: "+ self.message)
        print("length of message: " + str(self.lenMessage))
        return self.username, self.likes,self.replys,self.retweets,self.message,self.lenMessage
