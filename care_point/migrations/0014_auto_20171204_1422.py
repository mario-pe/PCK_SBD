# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care_point', '0013_auto_20171204_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decision',
            name='ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='care_point.Ward'),
        ),
    ]
