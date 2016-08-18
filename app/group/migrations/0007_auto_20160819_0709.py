# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 22:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0006_group_member'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('group', 'member')]),
        ),
    ]
