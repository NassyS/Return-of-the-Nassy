#!/usr/bin/python

import tweepy
import datetime
import requests
import os
os.chdir('/bin/rsnotif')
from loaders import *
from notifier import *

now = datetime.datetime.now()

# twitter API keys
consumer_key, consumer_secret, access_token, access_token_secret = getTwitterKeys()

# OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Grab 5 newest tweets
new_tweets = api.user_timeline(screen_name = "JagexClock", count=5)

urls = getUrls('spotlight')
for tweet in new_tweets:
    if 'spotlighted' in tweet.text:
        notify('spotlight', urls, tweet.text)
