# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin, messages
from django.utils.translation import ugettext as _
from . import models


@admin.register(models.SimpleNews)
class SimpleNewsAdmin(admin.ModelAdmin):
    model = models.SimpleNews

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()

@admin.register(models.SimpleCatNews)
class SimpleCatNewsAdmin(admin.ModelAdmin):
    model = models.SimpleCatNews

