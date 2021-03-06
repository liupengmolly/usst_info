# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jwcinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.CharField(blank=True, max_length=20000, null=True)),
                ('crawltime', models.DateTimeField()),
                ('releasetime', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
            options={
                'db_table': 'jwcinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
            ],
        ),
    ]
