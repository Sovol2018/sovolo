# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 01:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0041_auto_20170825_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='admin',
            field=models.ManyToManyField(blank=True, related_name='admin_skill', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(default='ボランティアできること'),
        ),
    ]