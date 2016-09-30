# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0003_otheruser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otheruser',
            old_name='user_data',
            new_name='profiles',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_data',
            new_name='profiles',
        ),
    ]
