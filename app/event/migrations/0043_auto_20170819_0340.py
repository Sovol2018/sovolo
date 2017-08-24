# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0042_auto_20170819_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='latitude',
            field=models.FloatField(blank=True, default=139.7191, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='longitude',
            field=models.FloatField(blank=True, default=35.7291, null=True),
        ),
    ]