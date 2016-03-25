# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0005_remove_model_about_about_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_about',
            name='about_pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2016, 3, 24, 21, 40, 50, 562965, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model_about',
            name='about_text',
            field=models.TextField(max_length=1000, default='hehehehe'),
            preserve_default=False,
        ),
    ]
