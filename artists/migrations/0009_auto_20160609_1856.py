# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0028_merge'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('home', '0002_auto_20160605_1702'),
        ('artists', '0008_auto_20160605_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artworkattributionlink',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='artworkattributionlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='artworkattributionlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='artworkpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='artworkpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='ArtworkAttributionLink',
        ),
        migrations.DeleteModel(
            name='ArtworkPage',
        ),
    ]