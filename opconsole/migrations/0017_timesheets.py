# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opconsole', '0016_auto_20170413_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timesheets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=255)),
                ('recptTime', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField()),
                ('devTz', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('status', models.CharField(choices=[(0, b'ACCEPTED'), (1, b'REFUSED_WRONG_TZ'), (2, b'REFUSED_DEV_DATA_MISMATCH'), (3, b'REFUSED_NOT_IN_ZONE'), (4, b'USER_DEACTIVATED')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opconsole.Employes')),
            ],
        ),
    ]
