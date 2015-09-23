""" prints the twitter timeline of a user """

from sys import argv
from histogram import histogram, inv_dict, most_freq, sort_dct
from utils import ununicode, unescape, parser, get_hashtags, \
            get_mentions, get_tweets, get_tweet

def extract_tweets(tweets):
    """ prints the tweets from tweets: list of tweet dicts """
    tweet_texts = []
    for tweet in tweets:
        text = get_tweet(tweet)
        text = text.encode('unicode-escape')
        text = ununicode(text)
        text = unescape(text)
        tweet_texts.append(parser(text))
    return tweet_texts

def print_stats(stat_lst, count=2):
    """ prints count number of stats:list of tuples
        of the form (data, count)
    """
    if len(stat_lst) == 0:
        print 'Empty: No stats available!'
    else:
        if len(stat_lst) < count:
            count = len(stat_lst)
            print 'there is only', count, 'stats'

        idx = 0
        for dummy_ in range(count):
            print stat_lst[idx][0],  stat_lst[idx][1]
            idx += 1
    print


def get_stats(tweets, count=2):
    """ prints stats about hashtags and user mentions """
    print 'Statistics\n-----------------------'
    hashtags = get_hashtags(tweets)
    mentions = get_mentions(tweets)
    
    freq_hashtags =  sort_dct(histogram(hashtags))
    freq_mentions =  sort_dct(histogram(mentions))
    return freq_hashtags[:count], freq_mentions[:count]

def main():
    """ prints timeline  and stats"""
    if len(argv) != 4:
        print 'usage: tweets.py screen_name tweet_count stat_count'
        return
    scr_name = argv[1]
    twt_count, stat_count = int(argv[2]), int(argv[3])
    tweets = get_tweets(scr_name, twt_count)
    #print extract_tweets(tweets)
    print len(tweets), 'tweets displayed'
    get_stats(tweets, stat_count)
    

if  __name__ == '__main__':
    main()
