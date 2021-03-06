# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-10 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Core', '0004_auto_20160710_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('completion_year',
                 models.IntegerField(default=None, null=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
