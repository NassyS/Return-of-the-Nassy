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

for tweet in new_tweets:
    if now.hour == tweet.created_at.hour:
	if "Amlodd" in tweet.text:
            notify('amlodd', urls)
        if "Cadarn" in tweet.text:
            notify('cadarn', urls)
        if "Crwys" in tweet.text:
            notify('crwys', urls)
	if "Ithell" in tweet.text:
            notify('ithell', urls)
        if "Iorwerth" in tweet.text:
            notify('iorwerth', urls)
	if "Trah" in tweet.text:
            notify('trah', urls)
	if "Meilyr" in tweet.text:
            notify('meilyr', urls)
       	if "Hefin" in tweet.text:
            notify('hefin', urls)
