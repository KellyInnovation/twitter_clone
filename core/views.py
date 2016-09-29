from django.shortcuts import render

from django.contrib.auth.models import User
from tweets.models import Tweet


def index(request):
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

	return render(request, "core/index.html", context)
