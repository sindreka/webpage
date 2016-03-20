# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0002_auto_20160320_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model_about',
            old_name='headline',
            new_name='about_headline',
        ),
        migrations.RenameField(
            model_name='model_about',
            old_name='pub_date',
            new_name='about_pub_date',
        ),
        migrations.RenameField(
            model_name='model_about',
            old_name='text',
            new_name='about_text',
        ),
        migrations.RenameField(
            model_name='model_home',
            old_name='pub_date',
            new_name='home_pub_date',
        ),
    ]
