# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_auto_20160605_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistprofilepage',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]