from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from core.forms import BootstrapFormMixin

class LoginForm(BootstrapFormMixin, AuthenticationForm):
	pass

class UserRegistrationForm(BootstrapFormMixin, forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password', 'first_name', 'last_name', 'email')

	