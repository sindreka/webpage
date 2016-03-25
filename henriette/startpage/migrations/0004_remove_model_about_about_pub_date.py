# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0003_auto_20160320_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_about',
            name='about_pub_date',
        ),
    ]
