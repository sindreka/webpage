# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0009_edit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='edit',
        ),
    ]
