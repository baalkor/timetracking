# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opconsole', '0015_auto_20170412_2142'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClientSoftware',
        ),
        migrations.AlterUniqueTogether(
            name='devicemodel',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='devicemodel',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='devicemodel',
            name='os',
        ),
        migrations.RemoveField(
            model_name='device',
            name='devModel',
        ),
        migrations.AddField(
            model_name='device',
            name='deviceData',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Brands',
        ),
        migrations.DeleteModel(
            name='DeviceModel',
        ),
    ]
