# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 23:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0033_auto_20160820_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='supporter',
            field=models.ManyToManyField(blank=True, related_name='support', to=settings.AUTH_USER_MODEL),
        ),
    ]
