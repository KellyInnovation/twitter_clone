from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Tweet
from .forms import TweetForm
from django.contrib.auth.models import User
from user_profiles.models import UserProfile
from django.contrib.auth.decorators import login_required


def tweet_display(request):
	tweets = Tweet.objects.all()
	users = User.objects.all()
	profiles = UserProfile()
	form = TweetForm()

	context = {
		"tweets": tweets,
		"users": users,
		"profiles":profiles,
		"form":form,
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

@login_required
def tweet_new(request):
	profiles = UserProfile()

	if request.method == "POST":
		form = TweetForm(request.POST)
		if form.is_valid():
			tweet_text = form.save(commit=False)
			tweet_text.user = request.user
			tweet_text.profile = profiles.id

			tweet_text.save()
			messages.success(request, "Tweet created!")

			return redirect("tweets:tweet_display")

	else:
		form = TweetForm()

	context = {
		"form": form,
	}

	return render(request, "tweets/tweet_new.html", context)