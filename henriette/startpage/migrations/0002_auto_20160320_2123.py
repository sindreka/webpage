# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_about',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('headline', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='model_home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('home_text', models.TextField(max_length=1000)),
                ('home_headline', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Startpage',
        ),
    ]
