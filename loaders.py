#!/usr/bin/python

import csv
from csv import DictReader
from csv import reader

def getUrls(x):
    urlDict = {}
    with open("webhooks.csv") as f:
        names = [row['name'] for row in DictReader(f)]
    with open("webhooks.csv") as f:
        urls = [row[x] for row in DictReader(f)]
    for i in range(0, len(names)):
        urlDict[str(names[i])] = urls[i]
    return urls

def getRoles():
    roleDict = {}
    with open('roles.csv') as f:
        myReader = reader(f)
        roles = next(myReader)
    for role in roles:
        with open('roles.csv') as f:
            ids = [row[role] for row in DictReader(f)]
            roleDict[role] = ids
    return roleDict

