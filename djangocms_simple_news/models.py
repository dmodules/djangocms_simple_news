# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from djangocms_text_ckeditor.fields import HTMLField

from autoslug import AutoSlugField
from filer.fields.image import FilerImageField

class SimpleCatNews(models.Model):
    slug = AutoSlugField(populate_from='title', unique=True)
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = _('News cat')
        verbose_name_plural = _('News cats')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('simple_news_listview', kwargs={'slug': self.slug})

class SimpleNews(models.Model):
    slug = AutoSlugField(populate_from='title', unique=True)
    pub_date = models.DateField(verbose_name=_("Publication date"), null=True)
    title = models.CharField(max_length=250)
    image = FilerImageField(verbose_name=_("image"), null=True, blank=True)
    #description_image = FilerImageField(verbose_name=_("image description"), null=True, blank=True, related_name="new_desc_image")
    description = HTMLField(verbose_name=_("Description"), null=True, blank=True)
    published = models.BooleanField(verbose_name=_("Published"), default=True)
    cat = models.ForeignKey(SimpleCatNews, verbose_name=_("Categorie"), on_delete=models.CASCADE, null=True, blank=True)
    

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('simple_news_detailview', kwargs={'slug': self.slug})
