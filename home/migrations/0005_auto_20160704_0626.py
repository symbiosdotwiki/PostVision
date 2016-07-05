# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('home', '0004_auto_20160702_0331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='standardpage',
            options={'verbose_name': 'Standard Page'},
        ),
        migrations.RemoveField(
            model_name='standardpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='standardpage',
            name='background_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='standardpage',
            name='background_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AddField(
            model_name='standardpage',
            name='menu_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_carousel_items', to='home.StandardPage'),
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_related_links', to='home.StandardPage'),
        ),
    ]