# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opconsole', '0043_auto_20170524_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='absences',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='absences',
            name='type',
            field=models.CharField(choices=[(0, b'SICKNESS'), (1, b'HOLIDAY'), (2, b'MOVING')], max_length=1),
        ),
    ]
