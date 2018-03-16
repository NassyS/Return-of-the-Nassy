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

notif = str(sys.argv[1])

urls = getUrls(notif)

substrings = {'vos': ['Amlodd', 'Cadarn', 'Crwys', 'Ithell', 'Iorwerth', 'Trahaearn', 'Meilyr', 'Hefin'], 'raven': ['feathers', 'handsome', 'avian'], 'wbs': ['warbands'], 'spotlight': ['spotlight']}

for tweet in new_tweets:
    if notif == 'wbs' or notif == 'spotlight':
        msg = ' ' + tweet.text
    if notif == 'raven':
        msg = ' A raven has spawned in prif!'
    if notif == 'vos':
        if now.hour == tweet.created_at.hour:
            for string in substrings[notif]:
                if string in tweet.text:
                    msg = ' The Voice of Seren is now active in the ' + string + ' district.'
                    notify(string, urls, msg)
    else:
        for string in substrings[notif]:
            if string in tweet.text.lower():
                notify(notif, urls, msg)
