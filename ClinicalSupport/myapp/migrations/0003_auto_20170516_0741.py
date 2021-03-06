# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170516_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='allergies',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='asthma',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='breathlessness',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='cough',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='cvd',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='dm',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='fever',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='hemoptysis',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='hiv',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='sinusitis',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='skinrash',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='smokingHistory',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='clinicuserprofile',
            name='tb',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
