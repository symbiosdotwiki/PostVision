# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-22 14:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0009_auto_20160609_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistprofilelink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='artistprofilelink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='artistprofilelink',
            name='page',
        ),
        migrations.DeleteModel(
            name='ArtistProfileLink',
        ),
    ]