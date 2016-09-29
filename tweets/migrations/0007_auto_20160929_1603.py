# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_auto_20160928_1759'),
        ('tweets', '0006_tweet_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(to='user_profiles.UserProfile', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True, default=datetime.datetime(2016, 9, 29, 16, 3, 59, 148722, tzinfo=utc)),
        ),
    ]
