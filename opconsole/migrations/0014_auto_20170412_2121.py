# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 03:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opconsole', '0013_auto_20170411_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientSoftware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('version', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(0, b'INITIALIZED'), (1, b'DEACTIVATED'), (2, b'INSERTED')], default=2, max_length=1)),
                ('serial', models.CharField(max_length=255)),
                ('initDate', models.DateTimeField(blank=True)),
                ('timezone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opconsole.Brands')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opconsole.ClientSoftware')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='devModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opconsole.DeviceModel'),
        ),
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='clientsoftware',
            unique_together=set([('name', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='devicemodel',
            unique_together=set([('name', 'brand', 'os')]),
        ),
    ]
