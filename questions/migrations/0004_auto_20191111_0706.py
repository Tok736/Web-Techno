# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-11-11 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20191111_0646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
    ]