# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_auto_20160928_1759'),
        ('tweets', '0003_auto_20160927_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user_profile',
            field=models.ForeignKey(blank=True, to='user_profiles.UserProfile', null=True),
        ),
    ]
