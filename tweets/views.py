from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Tweet
from .forms import TweetForm

def tweet_list(request):
	tweets = Tweet.objects.all()

	context = {
		"tweets": tweets,
		
	}

	return render(request, "tweets/tweet_list.html", context)

def tweet_new(request):
	if request.method == "POST":
		form = TweetForm(request.POST)
		if form.is_valid():
			tweet = form.save()
			messages.success(request, "Tweet created!")
			return redirect("core:index")

	else:
		form = TweetForm()

	context = {
		"form": form,
	}

	return render(request, "tweets/tweet_new.html", context)