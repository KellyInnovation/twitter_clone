from django.contrib import admin

from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
	list_display = ['tweet_text', 'published_date', 'user']

admin.site.register(Tweet, TweetAdmin)
