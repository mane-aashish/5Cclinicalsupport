# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20170613_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiouserprofilechest',
            name='consolidation',
            field=models.CharField(default='NULL', max_length=400),
        ),
        migrations.AlterField(
            model_name='radiouserprofilechest',
            name='nodules',
            field=models.CharField(default='NULL', max_length=400),
        ),
    ]
