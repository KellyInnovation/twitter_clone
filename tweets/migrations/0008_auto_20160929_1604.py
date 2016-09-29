# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_auto_20160929_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
