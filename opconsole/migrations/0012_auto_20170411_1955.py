# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opconsole', '0011_auto_20170411_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zones',
            name='color',
            field=models.IntegerField(),
        ),
    ]
