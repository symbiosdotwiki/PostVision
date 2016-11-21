# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-21 02:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('contact', '0001_initial'),
        ('wagtailcore', '0028_merge'),
        ('links', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('home.standardpage',),
        ),
        migrations.AddField(
            model_name='sitesocialmediacontact',
            name='link_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AddField(
            model_name='sitesocialmediacontact',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='sitesocialmediacontact',
            name='link_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.RelatedLinkType', verbose_name='Link type'),
        ),
        migrations.AddField(
            model_name='sitesocialmediacontact',
            name='site',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='sitesocialmediacontact', to='wagtailcore.Page'),
        ),
    ]