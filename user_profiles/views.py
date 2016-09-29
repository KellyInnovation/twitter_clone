from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
from .models import UserProfile
from tweets.models import Tweet


def profile_list(request):
	users = User.objects.all()
	tweets = Tweet.objects.all()
	username = request.user.username
	full_name = "{} {}".format(request.user.first_name.title(), request.user.last_name.title())


	context = {
		"username": username,
		"full_name": full_name,
		"users": users,
		"tweets": tweets,
	}

	return render(request, "user_profiles/profile.html", context)

def following(request):
	pass

def can_edit(request):
	pass

def user_info(request):
	pass
