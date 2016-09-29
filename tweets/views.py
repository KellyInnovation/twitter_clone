from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Tweet
from .forms import TweetForm
from django.contrib.auth.models import User
from user_profiles.models import UserProfile

def tweet_display(request):
	tweets = Tweet.objects.all()
	users = User()
	profiles = UserProfile()
	username = profiles.username1

	context = {
		"tweets": tweets,
		"users": users,
		"profiles":profiles,
		"username": username,	
	}

	return render(request, "tweets/tweet_display.html", context)

def tweet_new(request):
	if request.method == "POST":
		form = TweetForm(request.POST)
		if form.is_valid():
			tweet_text = form.save()
			messages.success(request, "Tweet created!")
			return redirect("tweets:tweet_display")

	else:
		form = TweetForm()

	context = {
		"form": form,
	}

	return render(request, "tweets/tweet_new.html", context)