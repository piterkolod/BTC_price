# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-25 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='max_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='min_price',
        ),
        migrations.AddField(
            model_name='price',
            name='time',
            field=models.TimeField(default=None),
        ),
    ]
