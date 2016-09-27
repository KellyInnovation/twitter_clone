# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20160927_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet_text',
            field=models.CharField(max_length=140, default=' '),
        ),
    ]
