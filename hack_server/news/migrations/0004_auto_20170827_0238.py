# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title',
        ),
        migrations.AlterField(
            model_name='news',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Reporter'),
        ),
        migrations.AlterField(
            model_name='news',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
