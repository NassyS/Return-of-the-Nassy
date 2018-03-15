import requests
from loaders import *

def notify(x, urls, msg=False):
    roles = getRoles()
    ids = roles[x]
    for i in range(0, len(urls)):
        if urls[i] == None: continue
        message = ids[i] + str(msg) if msg else ids[i]
        if urls[i] != '':
           r = requests.post(urls[i], data={"content": message})
