# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care_point', '0015_auto_20171205_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worksheet',
            name='date_from',
        ),
        migrations.RemoveField(
            model_name='worksheet',
            name='date_to',
        ),
        migrations.AddField(
            model_name='worksheet',
            name='date',
            field=models.DateField(blank=True, default=b'2017-12-12', null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_from',
            field=models.DateField(blank=True, default=b'2017-12-12', null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_to',
            field=models.DateField(blank=True, default=b'2017-12-12', null=True),
        ),
    ]
