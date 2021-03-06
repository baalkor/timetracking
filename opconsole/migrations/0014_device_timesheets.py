# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opconsole', '0013_auto_20170411_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(0, b'INITIALIZED'), (1, b'DEACTIVATED'), (2, b'INSERTED')], default=2, max_length=1)),
                ('deviceData', models.CharField(max_length=255)),
                ('serial', models.CharField(max_length=255)),
                ('initDate', models.DateTimeField(blank=True)),
                ('timezone', models.CharField(max_length=255)),
                ('salt', models.IntegerField()),
                ('devKey', models.CharField(max_length=64)),
                ('phoneNumber', models.CharField(blank=True, max_length=255)),
                ('devType', models.CharField(choices=[(0, b'INITIALIZED'), (1, b'DEACTIVATED'), (2, b'INSERTED')], default=0, max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='opconsole.Employes')),
            ],
        ),
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
