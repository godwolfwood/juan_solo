# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_wish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hired_at',
            field=models.CharField(max_length=255),
        ),
    ]
