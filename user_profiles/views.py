from django.shortcuts import render, get_object_or_404

from .models import UserProfile

def profile_list(request):
	user_profile = UserProfile.objects.all()
	

	context = {
		"user_profile": user_profile,
	}

	return render(request, "user_profiles/profile.html", context)

def following(request):
	pass

def can_edit(request):
	pass


