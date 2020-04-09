import tweepy
import json
from langdetect import detect

client = open('client_secret.json',)
client_dictionary =json.load(client)
print(client_dictionary)
auth = tweepy.OAuthHandler(client_dictionary['consumer_key'], client_dictionary['consumer_secret'])
auth.set_access_token(client_dictionary['access token'],client_dictionary['access token secret'])
api = tweepy.API(auth)
'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
'''
