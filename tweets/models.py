from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
 

class Tweet(models.Model):	
	tweet_text = models.CharField(max_length=140, default=" ")
	

	def __str__(self):
		return self.tweet_text

	def get_absolute_url(self):
		return reverse('tweets:tweet_list', args=[self.pk])




