from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.tweet_display, name='tweet_display'),
	url(r'new/$', views.tweet_new, name='tweet_new'),
]