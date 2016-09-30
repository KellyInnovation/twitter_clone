from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Tweet
from .forms import TweetForm
from django.contrib.auth.models import User
from user_profiles.models import UserProfile

def tweet_display(request):
	tweets = Tweet.objects.all()
	users = User.objects.all()
	profiles = UserProfile()
	full_name = "{} {}".format(request.user.first_name.title(), request.user.last_name.title())


	context = {
		"tweets": tweets,
		"users": users,
		"profiles":profiles,
		"full_name": full_name,
	}

	return render(request, "tweets/tweet_display.html", context)

def tweet_list(request):
	tweets = Tweet.objects.all()
	users = User.objects.all()
	profiles = UserProfile()


	context = {
		"tweets": tweets,
		"users": users,
		"profiles":profiles,
	
	}

	return render(request, "tweets/tweet_list.html", context)

def tweet_new(request):
	if request.method == "POST":
		form = TweetForm(request.POST)
		if form.is_valid():
			tweet_text = form.save(commit=False)
			tweet_text.user = request.user_id

			tweet_text.save()
			messages.success(request, "Tweet created!")

			return redirect("tweets:tweet_display")

	else:
		form = TweetForm()

	context = {
		"form": form,
	}

	return render(request, "tweets/tweet_new.html", context)