# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0009_auto_20160929_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
