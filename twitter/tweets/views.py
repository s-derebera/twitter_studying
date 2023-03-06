from django.shortcuts import render, redirect
from .models import Tweet
from django.shortcuts import render
from .forms import TweetForm


def index(request):
    latest_tweet_list = Tweet.objects.order_by('-pub_date')[:5]
    context = { 'latest_tweet_list': latest_tweet_list}
    return render(request, "tweets/index.html", context)

def new(request):
    form = TweetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            tweet = form.save()
            tweet.save()
            return redirect('index')
    
    return render(request, "tweets/new.html", {"form": form})
