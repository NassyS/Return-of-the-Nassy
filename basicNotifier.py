#!/usr/bin/python
import os
import requests
import sys

os.chdir('/bin/rsnotif')

from notifier import *
from loaders import *

notif = str(sys.argv[1])

try:
    world = sys.argv[2]
except:
    world = False

phrases = {'cache': ' will open in 5 minutes.', 'sinks': ' will spawn in 5 minutes.', 'goebies': ' begins in 15 minutes.', 'yews': ' are starting on world ' + str(world) + '.'}

urls = getUrls(notif)

notify(notif, urls, phrases[notif])
