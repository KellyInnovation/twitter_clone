# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profiles', '0002_auto_20160928_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('user_data', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('following', 'Can see tweets in their feed'), ('can_edit', 'Can edit or delete a tweet')),
            },
        ),
    ]
