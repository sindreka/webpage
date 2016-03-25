# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0006_auto_20160324_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_about',
            name='about_text',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='model_home',
            name='home_text',
            field=models.CharField(max_length=1000),
        ),
    ]
