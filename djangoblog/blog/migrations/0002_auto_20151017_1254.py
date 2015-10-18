# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 12, 54, 12, 903386)),
            preserve_default=False,
        ),
    ]
