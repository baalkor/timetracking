# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 03:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opconsole', '0006_auto_20170410_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employes',
            name='email',
        ),
    ]
