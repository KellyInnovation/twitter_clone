# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_remove_tweet_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
