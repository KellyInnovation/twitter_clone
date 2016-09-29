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


	def get_absolute_url(self):
		return reverse('user_profiles:profile', args=[self.pk])
