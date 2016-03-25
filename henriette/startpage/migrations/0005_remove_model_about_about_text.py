# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0004_remove_model_about_about_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_about',
            name='about_text',
        ),
    ]
