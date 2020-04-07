# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-11-05 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
        migrations.AddField(
            model_name='question',
            name='dislikes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='questions.Tag'),
        ),
    ]