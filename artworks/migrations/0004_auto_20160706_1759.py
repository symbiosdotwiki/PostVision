# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-06 17:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0003_artworkpage_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworkpage',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Post date'),
        ),
    ]
