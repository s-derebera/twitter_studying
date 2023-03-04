from django.shortcuts import render
from .models import Tweet
from django.shortcuts import render

def index(request):
    latest_tweet_list = Tweet.objects.order_by('-pub_date')[:5]
    context = { 'latest_tweet_list': latest_tweet_list}
    return render(request, "tweets/index.html", context)