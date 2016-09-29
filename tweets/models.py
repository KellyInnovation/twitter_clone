from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

from django.contrib.auth.models import User
from user_profiles.models import UserProfile

class Tweet(models.Model):	
	tweet_text = models.CharField(max_length=140, default=" ")
	published_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)

	def __str__(self):
		return self.tweet_text

	def get_absolute_url(self):
		return reverse('tweets:tweet_display', args=[self.pk])

	def user_info(self):
		pass


