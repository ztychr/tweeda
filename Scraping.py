from bs4 import BeautifulSoup
import requests
import Post

class Scraping:
    def __init__(self, tHandle, postamounts):

        self.tHandle = tHandle
        self.postamounts = postamounts
        self.r = requests.get('https://twitter.com/' + tHandle)

    def scrape_data(self):
        self.bs = BeautifulSoup(self.r.content, 'lxml')
        self.find_tweets = self.bs.find_all('div', {'class': 'tweet'})
        self.tweetlist = []

        if self.find_tweets:
            for tweet in self.find_tweets[:self.postamounts]:
                self.context = tweet.find('div', {'class': 'context'}).text.replace("\n", " ").strip()
                self.content = tweet.find('div', {'class': 'content'})
                self.header = self.content.find('div', {'class': 'stream-item-header'})
                self.userName = self.header.find('a', {
                    'class': 'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace(
                    "\n", " ").strip()
                self.timeTweeted = self.header.find('a', {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'}).find(
                    'span').text.replace("\n", " ").strip()

                self.userMessage = self.content.find('div', {'class': 'js-tweet-text-container'}).text.replace("\n", " ").strip()

                self.footer = self.content.find('div', {'class': 'stream-item-footer'})

                self.statistical = self.footer.find('div', {'class': 'ProfileTweet-actionCountList u-hiddenVisually'})
                self.likeSpan = self.statistical.find('span',{'class': 'ProfileTweet-action--favorite u-hiddenVisually'}).text.replace(  "\n", " ").strip()
                self.retweetspan = self.statistical.find('span',{'class': 'ProfileTweet-action--retweet u-hiddenVisually'}).text.replace("\n", " ").strip()
                self.replyspan = self.statistical.find('span',{'class': 'ProfileTweet-action--reply u-hiddenVisually'}).text.replace("\n", " ").strip()

                self.likes = int(''.join(i for i in self.likeSpan if i.isdigit()))
                self.retweets = int(''.join(i for i in self.retweetspan if i.isdigit()))
                self.replys = int(''.join(i for i in self.replyspan if i.isdigit()))

                self.temp_tweet = Post.tweet(self.userName, self.likes, self.replys, self.retweets, self.userMessage)
                self.tweetlist.append(self.temp_tweet)

               # if self.context:
               # print("context:", self.context)
               # print(self.temp_tweet.get_userName(), self.timeTweeted)
               # print("length of message: " + str(self.temp_tweet.lenMessage))
               # print(self.temp_tweet.get_message())
               # print("Lkes: " + str(self.temp_tweet.get_likes()))
               # print("retweets: " + str(self.temp_tweet.get_retweets()))
               # print("replys: " + str(self.temp_tweet.get_replys()))
               # print("amount of mentions in post: " + str(self.temp_tweet.mentions))
               # print("amount of hastags in this post" + str(self.temp_tweet.hastags))
               # print()


        else:
            print("User not found")

    def get_posts(self):
        if self.tweetlist:

            return self.tweetlist
        else:
            return "run scrapedata first"