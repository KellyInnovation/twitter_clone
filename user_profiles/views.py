from django.shortcuts import render, get_object_or_404

from .models import UserProfile

def profile_list(request):
	username = None

	if request.user.is_authenticated():
		username = request.user.username

	context = {
		"username": username,
	}

	return render(request, "user_profiles/profile.html", context)

def following(request):
	pass

def can_edit(request):
	pass

def user_info(request):
	pass
