import requests
from bs4 import BeautifulSoup

import Post

"""
The scraping class targets the individual div classes to fin¨¨¨¨ specific data about the tweets
    appends the data to a tweet_list
"""

class Scraping:
    """
    the constructor. intializes the name and amount of tweets.
    r performs the HTTP-request
    """

class Scraping:
    def __init__(self, tHandle, postamounts):

        self.tHandle = tHandle
        self.postamounts = postamounts
        self.r = requests.get('https://twitter.com/' + tHandle)

    """
    This method performs a scrape for the scrape object, and creates a list of tweets
    """
    def scrape_data(self):
        # Scrapes our data. Needs to be run before any other methods are
        self.bs = BeautifulSoup(self.r.content, 'html.parser')
        print("\n")
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
                self.li = tweet.find('li', {'class': 'js-stream-item stream-item stream-item'})

                self.id = tweet["data-tweet-id"]
                self.timeTweeted = self.header.find('a',
                                                    {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'}).find(
                    'span').text.replace("\n", " ").strip()
                self.userMessage = self.content.find('div', {'class': 'js-tweet-text-container'}).text.replace("\n",
                                                                                                               " ").strip()
                self.footer = self.content.find('div', {'class': 'stream-item-footer'})
                self.statistical = self.footer.find('div', {'class': 'ProfileTweet-actionCountList u-hiddenVisually'})
                self.likeSpan = self.statistical.find('span', {
                    'class': 'ProfileTweet-action--favorite u-hiddenVisually'}).text.replace("\n", " ").strip()
                self.retweetspan = self.statistical.find('span', {
                    'class': 'ProfileTweet-action--retweet u-hiddenVisually'}).text.replace("\n", " ").strip()
                self.replyspan = self.statistical.find('span', {
                    'class': 'ProfileTweet-action--reply u-hiddenVisually'}).text.replace("\n", " ").strip()
                self.likes = int(''.join(i for i in self.likeSpan if i.isdigit()))
                self.retweets = int(''.join(i for i in self.retweetspan if i.isdigit()))
                self.replys = int(''.join(i for i in self.replyspan if i.isdigit()))
                self.temp_tweet = Post.tweet(self.userName, self.likes, self.replys, self.retweets, self.userMessage, self.id)
                self.tweetlist.append(self.temp_tweet)

        else:
            print("User not found")

    """
    :returns the list that is generated from scrape_data()
    """

    def get_posts(self):
        # Gets our list of posts. scrape_data() needs to be run before this method
        if self.tweetlist:
            return self.tweetlist
        else:
            return print("run scrapedata first")
