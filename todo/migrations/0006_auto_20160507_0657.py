# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_deletedtodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deletedtodo',
            name='creator',
        ),
        migrations.AddField(
            model_name='todo',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='DeletedToDo',
        ),
    ]