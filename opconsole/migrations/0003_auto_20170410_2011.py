# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opconsole', '0002_auto_20170410_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='employes',
            name='email',
            field=models.EmailField(default='toto@toto.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employes',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
