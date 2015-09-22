""" utilities """

import re
import requests
from requests_oauthlib import OAuth1
from HTMLParser import HTMLParser as parser

parser = parser().unescape

APP_KEY = 'LygFznM7If85hSM6bUxiVLi2t'
APP_SECRET = 'INXtZ3OJ5IttsSJ9KrhwVPWdaL9SVvK4p2elD6nr5QiZfdwwVp'

def ununicode(text):
    """ removes unicode combinations """
    pat = r'http:\\u\d+'
    pat1 = r'\\u\d+'
    text = re.sub(pat, '', text) 
    text = re.sub(pat1, '', text) 
    return text


def unescape(text):
    """ reinstate \n ans \t s """
    text = re.sub(r'\\n', '\n', text) 
    text = re.sub(r'\\t', '\t', text) 
    return text


def get_tweets(scr_name, twt_count=5):
    """ prints the time line of the scr_name screen name """
    auth = OAuth1(APP_KEY, APP_SECRET)
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {'screen_name': scr_name, 'count': twt_count}

    r = requests.get(url, params=params, auth=auth)
    r.raise_for_status() #raises bad_request error if occurred
    rjson = r.json()
    return rjson


def print_tweets(tweets):
    """ prints the tweets from tweets: list of tweet dicts """
    print
    for tweet in tweets:
        text = tweet['text'].encode('unicode-escape')
        text = ununicode(text)
        text = unescape(text)
        print parser(text)
        print


def get_hashtags(tweets):
    """ return hashtags as a list """
    for tweet in tweets:
        for hashtag in tweet['entities']['hashtags']:
            yield hashtag['text']


def get_mentions(tweets):
    """ return hashtags as a list """
    for tweet in tweets:
        for mention in tweet['entities']['user_mentions']:
            yield mention['screen_name']


if  __name__ == '__main__':
    print 'main' 
