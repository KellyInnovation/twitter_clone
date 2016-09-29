from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


from user_profiles.models import UserProfile

class Tweet(models.Model):	
	tweet_text = models.CharField(max_length=140, default=" ")
	published_date = models.DateTimeField(null=True, blank=True)
	user = models.ForeignKey('user_profiles.UserProfile', null=True, blank=True)

	def __str__(self):
		return self.tweet_text

	def get_absolute_url(self):
		return reverse('tweets:tweet_display', args=[self.pk])

	def user_info(self):
		pass


