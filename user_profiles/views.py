from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
from .models import UserProfile, OtherUser
from tweets.models import Tweet
from tweets.forms import TweetForm


def profile_list(request):
	users = User.objects.all()
	tweets = Tweet.objects.all()
	username = request.user.username
	full_name = "{} {}".format(request.user.first_name.title(), request.user.last_name.title())
	form = TweetForm()

	context = {
		"username": username,
		"full_name": full_name,
		"users": users,
		"tweets": tweets,
		"form":form,
	}

	return render(request, "user_profiles/profile.html", context)

def other_profile(request, id):
	other_user = get_object_or_404(User, pk=id)
	users = User.objects.all()
	tweets = Tweet.objects.all()

	context = {
		"users": users,
		"tweets": tweets,
		"other_user": other_user,
	}

	return render(request, "user_profiles/other_profile.html", context)


def following(request):
	pass

def can_edit(request):
	pass

def user_info(request):
	pass
