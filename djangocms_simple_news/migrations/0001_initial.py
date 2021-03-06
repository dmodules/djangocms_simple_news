# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-17 12:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publised', models.BooleanField(default=True, verbose_name='Publié')),
                ('pub_date', models.DateField(auto_now=True, null=True, verbose_name='Publication date')),
                ('title', models.TextField(null=True, verbose_name='Titre')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Description')),
                ('page_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Page ID Link')),
                ('website_link', models.URLField(blank=True, null=True, verbose_name='Website Link ')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator user name ')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Title image')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
