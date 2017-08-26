# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 10:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0055_auto_20170826_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreviewlist',
            name='rating',
            field=models.IntegerField(choices=[(3, '3'), (2, '2'), (1, '1'), (4, '4'), (5, '5')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]