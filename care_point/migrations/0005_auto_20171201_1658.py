# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care_point', '0004_auto_20171130_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='decision',
        ),
        migrations.RemoveField(
            model_name='illness',
            name='decision',
        ),
        migrations.AddField(
            model_name='decision',
            name='activity',
            field=models.ManyToManyField(blank=True, null=True, to='care_point.Activity'),
        ),
        migrations.AddField(
            model_name='decision',
            name='illness',
            field=models.ManyToManyField(blank=True, null=True, to='care_point.Illness'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_from',
            field=models.DateField(blank=True, default=b'2017-12-01', null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_to',
            field=models.DateField(blank=True, default=b'2017-12-01', null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='genre',
            field=models.CharField(choices=[(b'umowa', b'umowa'), (b'zlecenie', b'zlecenie')], default=b'umowa', max_length=20),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='data_to',
            field=models.DateField(blank=True, default=b'2017-12-01', null=True),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='date_from',
            field=models.DateField(blank=True, default=b'2017-12-01', null=True),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='genre',
            field=models.CharField(choices=[(b'umowa', b'umowa'), (b'zlecenie', b'zlecenie')], default=b'umowa', max_length=15),
        ),
    ]
