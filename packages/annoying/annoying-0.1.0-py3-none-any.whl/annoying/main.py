import re
import pandas as pd
from textblob import TextBlob
import tweepy
from tweepy import OAuthHandler


df = pd.read_csv('vaccination_tweets.csv')

tweet_content = df.text
values = {}
list_sentiment = [] # a list of all the sentiments
def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'




def sentimentCreator():

#B
  
  for tweet in tweet_content:
    values['text'] = tweet
    values['sentiment'] = get_tweet_sentiment(tweet) #holds the value of the tweet

    list_sentiment.append(values['sentiment']) #adds the value to a list for c

#C
  df['sentiment'] = list_sentiment
  return df
sentimentCreator()
#4
def first30():
  print(df.head(30))
first30()

def calcPercentage():
  percent_dict = {
                  'positive': 0, 
                  'negative': 0, 
                  'neutral': 0,
                 }
  total = 0
  for sentiment in list_sentiment:
    if sentiment == 'positive':
      num = int(percent_dict['positive'])
      percent_dict['positive'] = num + 1
    elif sentiment == 'negative':
      num = int(percent_dict['negative'])
      percent_dict['negative'] = num + 1
    elif sentiment == 'neutral':
      num = int(percent_dict['neutral'])
      percent_dict['neutral'] = num + 1
    total = total + 1
      

  pos_num = int(percent_dict['positive'])
  neg_num = int(percent_dict['negative'])
  neu_num = int(percent_dict['neutral'])

  print("Positive: " + str(round((pos_num/total) * 100,2)) + "%")
  print("Negative: " + str(round((neg_num/total) * 100,2)) + "%")
  print(" Neutral: " + str(round((neu_num/total) * 100,2)) + "%")
  
calcPercentage()
