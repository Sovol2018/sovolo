# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0036_frame_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='region',
            field=models.CharField(choices=[('Hokkaido', 'Hokkaido'), ('Aomori', 'Aomori'), ('Iwate', 'Iwate'), ('Miyagi', 'Miyagi'), ('Akita', 'Akita'), ('Yamagata', 'Yamagata'), ('Fukushima', 'Fukushima'), ('Ibaraki', 'Ibaraki'), ('Tochigi', 'Tochigi'), ('Gunnma', 'Gunnma'), ('Saitama', 'Saitama'), ('Chiba', 'Chiba'), ('Tokyo', 'Tokyo'), ('Kanagawa', 'Kanagawa'), ('Niigata', 'Niigata'), ('Toyama', 'Toyama'), ('Ishikawa', 'Ishikawa'), ('Fukui', 'Fukui'), ('Yamanashi', 'Yamanashi'), ('Nagano', 'Nagano'), ('Gifu', 'Gifu'), ('Shizuoka', 'Shizuoka'), ('Aichi', 'Aichi'), ('Mie', 'Mie'), ('Shiga', 'Shiga'), ('Kyoto', 'Kyoto'), ('Osaka', 'Osaka'), ('Hyogo', 'Hyogo'), ('Nara', 'Nara'), ('Wakayama', 'Wakayama'), ('Tottori', 'Tottori'), ('Shimane', 'Shimane'), ('Okayama', 'Okayama'), ('Hiroshima', 'Hiroshima'), ('Yamaguchi', 'Yamaguchi'), ('Tokushima', 'Tokushima'), ('Kagawa', 'Kagawa'), ('Ehime', 'Ehime'), ('Kouchi', 'Kouchi'), ('Fukuoka', 'Fukuoka'), ('Saga', 'Saga'), ('Nagasaki', 'Nagasaki'), ('Kumamoto', 'Kumamoto'), ('Ooita', 'Ooita'), ('Miyazaki', 'Miyazaki'), ('Kagoshima', 'Kagoshima'), ('Okinawa', 'Okinawa')], max_length=10),
        ),
    ]
