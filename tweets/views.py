from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Tweet
from .forms import TweetForm
from django.contrib.auth.models import User

def tweet_list(request):
	tweets = Tweet.objects.all()
	users = User()

	context = {
		"tweets": tweets,
		"users": users
		
	}

	return render(request, "tweets/tweet_list.html", context)

def tweet_new(request):
	if request.method == "POST":
		form = TweetForm(request.POST)
		if form.is_valid():
			tweet_text = form.save()
			messages.success(request, "Tweet created!")
			return redirect("tweets:tweet_list")

	else:
		form = TweetForm()

	context = {
		"form": form,
	}

	return render(request, "tweets/tweet_new.html", context)