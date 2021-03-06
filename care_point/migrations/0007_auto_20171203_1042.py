# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care_point', '0006_auto_20171201_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ward',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='care_point.Ward'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_from',
            field=models.DateField(blank=True, default=b'2017-12-03', null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_to',
            field=models.DateField(blank=True, default=b'2017-12-03', null=True),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='data_to',
            field=models.DateField(blank=True, default=b'2017-12-03', null=True),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='date_from',
            field=models.DateField(blank=True, default=b'2017-12-03', null=True),
        ),
    ]
