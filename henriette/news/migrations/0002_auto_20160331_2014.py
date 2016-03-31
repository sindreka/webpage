# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_links',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('links_title', models.CharField(max_length=200)),
                ('links_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
