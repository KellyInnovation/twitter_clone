from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user_data = models.OneToOneField(User)
	

	class Meta:
		permissions = (
			("following", "Can see tweets in their feed"),
			("can_edit", "Can edit or delete a tweet"),
		)

		

	def __str__(self):
		return "{} {}".format(self.user_data.first_name, self.user_data.last_name)
		return self.user_data

	def get_absolute_url(self):
		return reverse('user_profiles:profile', args=[self.pk])
