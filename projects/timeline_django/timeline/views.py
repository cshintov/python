from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from tweets import extract_tweets, get_tweets, get_stats


def index(request):
    return HttpResponse("Hello, world. You're at timeline site.")

def get_input(request):
    return render(request, 'timeline/get_input.html')

def result(request, tweets, hash_tags, mentions):
    context =  {'tweets': tweets, 'hash_tags': hash_tags, 'mentions': mentions}
    return render(request, 'timeline/result.html', context)

def show_tweets(request):
    scr_name= request.POST.get("screen_name")
    twt_count = int(request.POST.get("tweet_count"))
    stat_count = int(request.POST.get("stat_count"))
    tweets = get_tweets(scr_name, twt_count)
    hash_tags, mentions = get_stats(tweets, stat_count)
    tweets = extract_tweets(tweets)
    return result(request, tweets, hash_tags, mentions)

