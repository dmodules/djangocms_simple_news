# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import SimpleNews, SimpleCatNews
from django.views.generic import ListView, DetailView


class SimpleNewsListView(ListView):
    model = SimpleNews
    template_name = "liste_nouvelles.html"
    context_object_name = 'simplenews'
    queryset = SimpleNews.objects.filter(published=True).order_by('-pub_date')
    context_object_name = "news_list"    #default is object_list as well as model's_verbose_name_list and/or model's_verbose_name_plural_list, if defined in the model's inner Meta class
    paginate_by = 10  #and that's it !!

    def get_context_data(self, *args, **kwargs):
        context = super(SimpleNewsListView, self).get_context_data(*args, **kwargs)

        if self.kwargs.get('slug'):
            context['categorie'] = SimpleCatNews.objects.get(slug=self.kwargs.get('slug'))
		
        return context

    def get_queryset(self):

        qs = self.model.objects.all()
        if self.kwargs.get('slug'):
            cat = SimpleCatNews.objects.get(slug=self.kwargs.get('slug'))
            qs = qs.filter(cat=cat, published=True).order_by('-pub_date')
        else:
            qs = qs.filter(published=True).order_by('-pub_date')

        return qs

class SimpleNewsDetailView(DetailView):
    model = SimpleNews
    template_name = "detail_nouvelles.html"
    context_object_name = 'simplenews'