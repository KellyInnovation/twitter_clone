# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='user_profile',
        ),
    ]
