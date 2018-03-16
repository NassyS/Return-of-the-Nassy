#!/usr/bin/python

import tweepy
import datetime
import requests
import os
import sys
os.chdir(sys.path[0])
from notifier import *
from loaders import *

now = datetime.datetime.now()

# twitter API keys
consumer_key, consumer_secret, access_token, access_token_secret = getTwitterKeys()

# OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Grab 5 newest tweets
new_tweets = api.user_timeline(screen_name = "JagexClock", count=10)

urls = getUrls('raven')

for tweet in new_tweets:
    if "perfectly glistening feathers" in tweet.text or "fantastically handsome" in tweet.text or "avian that you" in tweet.text:
        notify('raven', urls, ' A raven has spawned in prif!')
