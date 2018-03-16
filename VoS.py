#!/usr/bin/python

import tweepy
import datetime
import requests
import os
import sys
os.chdir(sys.path[0])
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

urls = getUrls("vos")

voices = ['amlodd', 'cadarn', 'crwys', 'ithell', 'iorwerth', 'trah', 'meilyr', 'hefin']

for tweet in new_tweets:
    if now.hour == tweet.created_at.hour:
        for voice in voices:
            if voice in tweet.text.lower():
                notify(voice, urls)
