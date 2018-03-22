# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-04 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_person_ip_addr'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='city_postal_code',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='country_code',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='dma_code',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='latitude',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='longitude',
            field=models.CharField(default='', max_length=100),
        ),
    ]
