from django.shortcuts import render, redirect
from .models import Tweet
from django.shortcuts import render
from .forms import TweetForm
from .models import Profile
from django.contrib import messages

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
    
    return render(request, "tweets/new.html", {"form":form})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, "tweets/profile_list.html", {"profiles": profiles})
    else:
        messages.success(request, ('You must be log in to see that page'))
        return redirect('index')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        if request.method == "POST":
            current_user = request.user.profile
            action = request.POST["follow"]
            if action == "follow":
                current_user.follows.add(profile)
            elif action == "unfollow":
                current_user.follows.remove(profile)
            current_user.save()
        

        return render(request, 'tweets/profile.html',{ "profile":profile})
    else:
        messages.success(request, ('Create your page firstful! Waitig for join us!'))
        return redirect('index')