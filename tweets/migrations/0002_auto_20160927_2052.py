# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='username',
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_text',
            field=models.CharField(null=True, max_length=140, blank=True),
        ),
    ]
