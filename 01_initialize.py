from requests_oauthlib import OAuth1Session
from requests.exceptions import ConnectionError, ReadTimeout, SSLError
import json, datetime, time, pytz, re, sys,traceback, pymongo
#from pymongo import Connection     # Connection classは廃止されたのでMongoClientに変更
from pymongo import MongoClient
from collections import defaultdict
import numpy as np

KEYS = {
        'consumer_key':'i9j9PufT5ZbxXnGf0PfPtcQd8',
        'consumer_secret':'1KSmatjwN6DVNT8EkaTQbmj3Ip0ZkDT14aXvInPvXx4IT7JioS',
        'access_token':'2392703516-adME4cAnx9MFB0UdaeJ8esOYvPVDuFGZ7lO0yXL',
        'access_secret':'oqkeeTRs7qhSt4eXujMt64taRu3VeShthGDWGeMpmijWM',
       }

twitter = None
connect = None
db      = None
tweetdata = None
meta    = None

def initialize(): # twitter接続情報や、mongoDBへの接続処理等initial処理実行
    global twitter, twitter, connect, db, tweetdata, meta
    twitter = OAuth1Session(KEYS['consumer_key'],KEYS['consumer_secret'],
                            KEYS['access_token'],KEYS['access_secret'])
# Connection classは廃止されたのでMongoClientに変更
    connect = MongoClient('localhost', 27017)
    db = connect.starbucks
    tweetdata = db.tweetdata
    meta = db.metadata

initialize()
