# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-26 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_simple_news', '0006_simplecatnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplenews',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangocms_simple_news.SimpleCatNews', verbose_name='Categorie'),
        ),
    ]
