# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opconsole', '0019_merge_20170501_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='tempCode',
            field=models.CharField(choices=[(0, b'INITIALIZED'), (1, b'DEACTIVATED'), (2, b'INSERTED')], default='24JSG', max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='serial',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
