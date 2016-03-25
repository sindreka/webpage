# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0010_delete_edit'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_edit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edit_boolean', models.BooleanField()),
            ],
        ),
    ]
