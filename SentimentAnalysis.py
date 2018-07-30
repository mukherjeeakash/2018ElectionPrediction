#2018 Midterm Elections Twitter Sentiment Analysis

'''
consumer_key = 'JVBdwwKQmtZZknIvcyN5gDWCQ'
consumer_secret = ' tI6sBGTS5J6hCSfavgK7iKf4XOpl3bDqalZeh8w7FM6oefPDMq'
access_token = '2153049373-rjS6369gks7rlAV1RmdHYCbbOfbLmmgGeh7XkY5'
access_token_secret = 'FfO8FDNR7uAQmTNUPLnlKJY6VQtoGKgc4tuEJFsSwUMZH'
'''

import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import pandas

#Code for the TwitterClient class is based on https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console (Replace these with your own)
        consumer_key = 'JVBdwwKQmtZZknIvcyN5gDWCQ'
        consumer_secret = 'tI6sBGTS5J6hCSfavgK7iKf4XOpl3bDqalZeh8w7FM6oefPDMq'
        access_token = '2153049373-rjS6369gks7rlAV1RmdHYCbbOfbLmmgGeh7XkY5'
        access_token_secret = 'FfO8FDNR7uAQmTNUPLnlKJY6VQtoGKgc4tuEJFsSwUMZH'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")


    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_query_sentiments(self, query, count = 10):
        '''
        Helper function to get general sentiments towards a particular query
        '''
        # Dictionary to store possible sentiments about a query
        sentiments = {'positive' : 0, 'negative' : 0, 'neutral' : 0}

        #Keeps track of parsed tweets to make sure that retweets are not parsed multiple times
        parsedTweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                if tweet not in parsedTweets:
                    sentiments[self.get_tweet_sentiment(tweet.text)] += 1
                    parsedTweets.append(tweet)

            #Converts sentiment values into percentages
            if (len(parsedTweets) > 0): #Some candidates have no tweets written about them. Avoids zero division error
                for key in sentiments:
                    sentiments[key] = round(sentiments[key] / len(parsedTweets), 4)

            sentiments["Tweets_Parsed"] = len(parsedTweets)

            return sentiments

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


    def get_queries_sentiments(self, queries, count = 10):
        '''
        Main function that returns a data frame containing the queries and sentiment percentages of the queries
        '''

        #Will be used to form the columns of the dataframe
        positive, negative, neutral, tweetsParsed = [], [], [], []

        for query in queries:
            sentiments = self.get_query_sentiments(query = query, count = count)
            positive.append(sentiments['positive'])
            negative.append(sentiments['negative'])
            neutral.append(sentiments['neutral'])
            tweetsParsed.append(sentiments['Tweets_Parsed'])

        sentimentData = pandas.DataFrame({
        "Query_Name" : queries,
        "Positive" : positive,
        "Negative" : negative,
        "Neutral" : neutral,
        'Tweets_Parsed' : tweetsParsed
        })

        return sentimentData


'''Main script'''
#Initialize TwitterClient object and read in senate data
api = TwitterClient()
senateData = pandas.read_csv('updated-senate-data.csv')

#Get sentiment percentages for each of the senate candidates as a dataframe
sentimentData = api.get_queries_sentiments(queries = senateData['Query_Name'], count = 5)

#Merge sentiment data with existing senate data and save as a csv file
senateData = pandas.merge(senateData, sentimentData, on = "Query_Name")
senateData.to_csv('updated-senate-data.csv')
