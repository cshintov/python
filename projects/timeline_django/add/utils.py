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


def find_max_id(tweets):
    """ 
    find the min id from the tweets in order to pass as the max_id
    to the  next request 
    tweets: list of dicts 
    """
    min_twt = lambda twt1, twt2: twt1 if twt1['id'] < twt2['id'] \
                                        else twt2
    bot_twt = reduce(min_twt, tweets)
    return bot_twt['id']


def get_tweets(scr_name, twt_count=5):
    """ prints the time line of the scr_name screen name """
    auth = OAuth1(APP_KEY, APP_SECRET)
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {'screen_name': scr_name, 'count': twt_count}

    resp = requests.get(url, params=params, auth=auth)
    resp.raise_for_status() #raises bad_request error if occurred
    tweets = resp.json()
    if twt_count <= 200 and len(tweets) <= 200:
        return tweets
    
    rest = twt_count - len(tweets)
    max_id = find_max_id(tweets) - 1
    while True:
        params = {'screen_name': scr_name, 'count': rest, 'max_id': max_id}
        resp = requests.get(url, params=params, auth=auth)
        resp.raise_for_status()
        new_twts = resp.json()
        tweets.extend(new_twts)
        if len(new_twts) < 100 or len(tweets) == twt_count:
            break
        max_id = find_max_id(tweets) - 1
        rest = twt_count - len(tweets)
    if len(tweets) < twt_count:
        params = {'screen_name': scr_name, 'count': twt_count - len(tweets), 'max_id': max_id}
        resp = requests.get(url, params=params, auth=auth)
        resp.raise_for_status()
        new_twts = resp.json()
        tweets.extend(new_twts)
    return tweets


def print_tweets(tweets):
    """ prints the tweets from tweets: list of tweet dicts """
    print
    for tweet in tweets:
        text = get_tweet(tweet)
        text = text.encode('unicode-escape')
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



def is_retweet(text):
    """ checks whether a tweet is a retweet """
    rtwt = r'^RT @'
    if re.search(rtwt, text):
        return True
    else:
        return False


def get_tweet(tweet):
    """ gets the tweet text from the tweet dict """
    text = tweet['text']
    if is_retweet(text):
        try:
            text = tweet['retweeted_status']['text']
        except:
            pass
    return text


if  __name__ == '__main__':
    print 'main' 
