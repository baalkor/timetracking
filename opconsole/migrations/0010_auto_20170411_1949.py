# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 01:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opconsole', '0009_zones_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zones',
            old_name='color',
            new_name='colors',
        ),
    ]