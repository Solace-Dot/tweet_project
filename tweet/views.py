from django.shortcuts import render, redirect
from .forms import TweetForm
from .models import Tweet

def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_tweets')
    else:
        form = TweetForm()
    return render(request, 'tweets/tweet_form.html', {'form': form})

def view_tweets(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})
