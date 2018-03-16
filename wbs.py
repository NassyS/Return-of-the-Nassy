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

consumer_key, consumer_secret, access_token_access_token_secret = getTwitterKeys()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

new_tweets = api.user_timeline(screen_name = "JagexClock", count=5)

urls = getUrls('wbs')

for tweet in new_tweets:
	if "Wilderness Warbands" in tweet.text:
            if now.hour == tweet.created_at.hour:
                notify('wbs', urls)
