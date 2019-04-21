# coding: utf-8

#Import Models

from djangocms_simple_news.models import SimpleCatNews
from django import template

register = template.Library()

@register.assignment_tag
def get_categories():
    news_cat = SimpleCatNews.objects.all().order_by('title')
    return news_cat
